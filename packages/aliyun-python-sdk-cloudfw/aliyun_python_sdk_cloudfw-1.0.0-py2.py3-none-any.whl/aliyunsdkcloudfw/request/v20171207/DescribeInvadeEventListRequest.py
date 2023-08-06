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

class DescribeInvadeEventListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'DescribeInvadeEventList','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProcessStatusLists(self): # RepeatList
		return self.get_query_params().get('ProcessStatusList')

	def set_ProcessStatusLists(self, ProcessStatusList):  # RepeatList
		for depth1 in range(len(ProcessStatusList)):
			self.add_query_param('ProcessStatusList.' + str(depth1 + 1), ProcessStatusList[depth1])
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_EventName(self): # String
		return self.get_query_params().get('EventName')

	def set_EventName(self, EventName):  # String
		self.add_query_param('EventName', EventName)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_AssetsInstanceId(self): # String
		return self.get_query_params().get('AssetsInstanceId')

	def set_AssetsInstanceId(self, AssetsInstanceId):  # String
		self.add_query_param('AssetsInstanceId', AssetsInstanceId)
	def get_EventKey(self): # String
		return self.get_query_params().get('EventKey')

	def set_EventKey(self, EventKey):  # String
		self.add_query_param('EventKey', EventKey)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_IsIgnore(self): # String
		return self.get_query_params().get('IsIgnore')

	def set_IsIgnore(self, IsIgnore):  # String
		self.add_query_param('IsIgnore', IsIgnore)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_CurrentPage(self): # String
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # String
		self.add_query_param('CurrentPage', CurrentPage)
	def get_AssetsIP(self): # String
		return self.get_query_params().get('AssetsIP')

	def set_AssetsIP(self, AssetsIP):  # String
		self.add_query_param('AssetsIP', AssetsIP)
	def get_RiskLevels(self): # RepeatList
		return self.get_query_params().get('RiskLevel')

	def set_RiskLevels(self, RiskLevel):  # RepeatList
		for depth1 in range(len(RiskLevel)):
			self.add_query_param('RiskLevel.' + str(depth1 + 1), RiskLevel[depth1])
	def get_MemberUid(self): # Long
		return self.get_query_params().get('MemberUid')

	def set_MemberUid(self, MemberUid):  # Long
		self.add_query_param('MemberUid', MemberUid)
	def get_EventUuid(self): # String
		return self.get_query_params().get('EventUuid')

	def set_EventUuid(self, EventUuid):  # String
		self.add_query_param('EventUuid', EventUuid)
	def get_AssetsInstanceName(self): # String
		return self.get_query_params().get('AssetsInstanceName')

	def set_AssetsInstanceName(self, AssetsInstanceName):  # String
		self.add_query_param('AssetsInstanceName', AssetsInstanceName)
