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

class DescribeRiskEventGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'DescribeRiskEventGroup','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcIP(self): # String
		return self.get_query_params().get('SrcIP')

	def set_SrcIP(self, SrcIP):  # String
		self.add_query_param('SrcIP', SrcIP)
	def get_RuleResult(self): # String
		return self.get_query_params().get('RuleResult')

	def set_RuleResult(self, RuleResult):  # String
		self.add_query_param('RuleResult', RuleResult)
	def get_RuleSource(self): # String
		return self.get_query_params().get('RuleSource')

	def set_RuleSource(self, RuleSource):  # String
		self.add_query_param('RuleSource', RuleSource)
	def get_DstNetworkInstanceId(self): # String
		return self.get_query_params().get('DstNetworkInstanceId')

	def set_DstNetworkInstanceId(self, DstNetworkInstanceId):  # String
		self.add_query_param('DstNetworkInstanceId', DstNetworkInstanceId)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_EventName(self): # String
		return self.get_query_params().get('EventName')

	def set_EventName(self, EventName):  # String
		self.add_query_param('EventName', EventName)
	def get_DataType(self): # String
		return self.get_query_params().get('DataType')

	def set_DataType(self, DataType):  # String
		self.add_query_param('DataType', DataType)
	def get_BuyVersion(self): # Long
		return self.get_query_params().get('BuyVersion')

	def set_BuyVersion(self, BuyVersion):  # Long
		self.add_query_param('BuyVersion', BuyVersion)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_DstIP(self): # String
		return self.get_query_params().get('DstIP')

	def set_DstIP(self, DstIP):  # String
		self.add_query_param('DstIP', DstIP)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_FirewallType(self): # String
		return self.get_query_params().get('FirewallType')

	def set_FirewallType(self, FirewallType):  # String
		self.add_query_param('FirewallType', FirewallType)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
	def get_VulLevel(self): # String
		return self.get_query_params().get('VulLevel')

	def set_VulLevel(self, VulLevel):  # String
		self.add_query_param('VulLevel', VulLevel)
	def get_AttackType(self): # String
		return self.get_query_params().get('AttackType')

	def set_AttackType(self, AttackType):  # String
		self.add_query_param('AttackType', AttackType)
	def get_SrcNetworkInstanceId(self): # String
		return self.get_query_params().get('SrcNetworkInstanceId')

	def set_SrcNetworkInstanceId(self, SrcNetworkInstanceId):  # String
		self.add_query_param('SrcNetworkInstanceId', SrcNetworkInstanceId)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_CurrentPage(self): # String
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # String
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_AttackApps(self): # RepeatList
		return self.get_query_params().get('AttackApp')

	def set_AttackApps(self, AttackApp):  # RepeatList
		for depth1 in range(len(AttackApp)):
			self.add_query_param('AttackApp.' + str(depth1 + 1), AttackApp[depth1])
	def get_NoLocation(self): # String
		return self.get_query_params().get('NoLocation')

	def set_NoLocation(self, NoLocation):  # String
		self.add_query_param('NoLocation', NoLocation)
