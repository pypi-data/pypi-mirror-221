# Copyright 2023 Clarifai, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Interface to Clarifai Models API."""

from typing import Type

from clarifai_grpc.grpc.api import resources_pb2, service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2, status_pb2
from google.protobuf import json_format

from clarifai.auth.helper import ClarifaiAuthHelper
from clarifai.client import create_stub


class BaseRunner:
  """
  Interface to Clarifai models api
  """

  def __init__(self, auth: Type[ClarifaiAuthHelper], runner_id: str) -> None:
    self.auth = auth
    self.stub = create_stub(self.auth)
    self.runner_id = runner_id

  def start(self):
    self._long_poll_loop()

  def run(self, item: service_pb2.PostModelOutputsRequest) -> service_pb2.MultiOutputResponse:
    """
    Run the model on the given item.
    """
    outputs = []
    for inp in item.inputs:
      outputs.append(self.run_input(inp))

    return service_pb2.MultiOutputResponse(
        status=status_pb2.Status(
            code=status_code_pb2.SUCCESS,
            description="Success",
        ),
        outputs=outputs,
    )

  def run_input(self, input: resources_pb2.Input) -> resources_pb2.Output:
    """
    Run the model on the given input.
    """
    raise NotImplementedError("run_input() not implemented")

  def _long_poll_loop(self):
    c = 0
    while True:
      # Long poll waiting for work.
      print("Loop iteration: {}".format(c))
      work_response = self.stub.ListRunnerItems(
          service_pb2.ListRunnerItemsRequest(
              user_app_id=self.auth.get_user_app_id_proto(), runner_id=self.runner_id))
      if work_response.status.code == status_code_pb2.RUNNER_NEEDS_RETRY:
        c += 1
        continue  # immediate restart the long poll
      if work_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Error getting work: {}".format(work_response.status.description))
      if len(work_response.items) == 0:
        print("No work to do. Waiting...")
        continue

      # We have work to do. Run the model on the inputs.
      for item in work_response.items:
        if not item.HasField('post_model_outputs_request'):
          raise Exception("Unexpected work item type: {}".format(item))
        print(
            f"Working on item: {item.id} with inputs {len(item.post_model_outputs_request.inputs)}"
        )
        result = self.run(item.post_model_outputs_request)

        result_response = self.stub.PostRunnerItemOutputs(
            service_pb2.PostRunnerItemOutputsRequest(
                user_app_id=self.auth.get_user_app_id_proto(),
                item_id=item.id,
                runner_id=self.runner_id,
                runner_item_outputs=[service_pb2.RunnerItemOutput(multi_output_response=result)]))
        if result_response.status.code != status_code_pb2.SUCCESS:
          raise Exception(
              json_format.MessageToJson(result_response, preserving_proto_field_name=True))
          # raise Exception("Error posting result: {}".format(result_response.status.description))
