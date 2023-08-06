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

class PutDisableFwSwitchRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'PutDisableFwSwitch','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceTypeLists(self): # RepeatList
		return self.get_query_params().get('ResourceTypeList')

	def set_ResourceTypeLists(self, ResourceTypeList):  # RepeatList
		for depth1 in range(len(ResourceTypeList)):
			self.add_query_param('ResourceTypeList.' + str(depth1 + 1), ResourceTypeList[depth1])
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_RegionLists(self): # RepeatList
		return self.get_query_params().get('RegionList')

	def set_RegionLists(self, RegionList):  # RepeatList
		for depth1 in range(len(RegionList)):
			self.add_query_param('RegionList.' + str(depth1 + 1), RegionList[depth1])
	def get_IpaddrLists(self): # RepeatList
		return self.get_query_params().get('IpaddrList')

	def set_IpaddrLists(self, IpaddrList):  # RepeatList
		for depth1 in range(len(IpaddrList)):
			self.add_query_param('IpaddrList.' + str(depth1 + 1), IpaddrList[depth1])
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
