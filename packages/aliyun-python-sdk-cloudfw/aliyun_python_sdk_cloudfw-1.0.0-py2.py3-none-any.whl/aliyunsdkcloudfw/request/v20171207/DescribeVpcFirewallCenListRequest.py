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

class DescribeVpcFirewallCenListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'DescribeVpcFirewallCenList','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_NetworkInstanceId(self): # String
		return self.get_query_params().get('NetworkInstanceId')

	def set_NetworkInstanceId(self, NetworkInstanceId):  # String
		self.add_query_param('NetworkInstanceId', NetworkInstanceId)
	def get_VpcFirewallName(self): # String
		return self.get_query_params().get('VpcFirewallName')

	def set_VpcFirewallName(self, VpcFirewallName):  # String
		self.add_query_param('VpcFirewallName', VpcFirewallName)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_VpcFirewallId(self): # String
		return self.get_query_params().get('VpcFirewallId')

	def set_VpcFirewallId(self, VpcFirewallId):  # String
		self.add_query_param('VpcFirewallId', VpcFirewallId)
	def get_RouteMode(self): # String
		return self.get_query_params().get('RouteMode')

	def set_RouteMode(self, RouteMode):  # String
		self.add_query_param('RouteMode', RouteMode)
	def get_CurrentPage(self): # String
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # String
		self.add_query_param('CurrentPage', CurrentPage)
	def get_FirewallSwitchStatus(self): # String
		return self.get_query_params().get('FirewallSwitchStatus')

	def set_FirewallSwitchStatus(self, FirewallSwitchStatus):  # String
		self.add_query_param('FirewallSwitchStatus', FirewallSwitchStatus)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_RegionNo(self): # String
		return self.get_query_params().get('RegionNo')

	def set_RegionNo(self, RegionNo):  # String
		self.add_query_param('RegionNo', RegionNo)
	def get_MemberUid(self): # String
		return self.get_query_params().get('MemberUid')

	def set_MemberUid(self, MemberUid):  # String
		self.add_query_param('MemberUid', MemberUid)
	def get_TransitRouterType(self): # String
		return self.get_query_params().get('TransitRouterType')

	def set_TransitRouterType(self, TransitRouterType):  # String
		self.add_query_param('TransitRouterType', TransitRouterType)
