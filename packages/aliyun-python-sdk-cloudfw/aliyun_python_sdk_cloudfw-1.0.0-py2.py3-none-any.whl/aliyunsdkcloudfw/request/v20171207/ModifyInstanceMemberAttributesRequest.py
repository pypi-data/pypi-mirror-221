# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcloudfw.endpoint import endpoint_data

class ModifyInstanceMemberAttributesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'ModifyInstanceMemberAttributes','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Memberss(self): # RepeatList
		return self.get_query_params().get('Members')

	def set_Memberss(self, Members):  # RepeatList
		for depth1 in range(len(Members)):
			if Members[depth1].get('MemberUid') is not None:
				self.add_query_param('Members.' + str(depth1 + 1) + '.MemberUid', Members[depth1].get('MemberUid'))
			if Members[depth1].get('MemberDesc') is not None:
				self.add_query_param('Members.' + str(depth1 + 1) + '.MemberDesc', Members[depth1].get('MemberDesc'))
