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

class CreateTrFirewallV2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'CreateTrFirewallV2','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_FirewallVswitchId(self): # String
		return self.get_query_params().get('FirewallVswitchId')

	def set_FirewallVswitchId(self, FirewallVswitchId):  # String
		self.add_query_param('FirewallVswitchId', FirewallVswitchId)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_FirewallSubnetCidr(self): # String
		return self.get_query_params().get('FirewallSubnetCidr')

	def set_FirewallSubnetCidr(self, FirewallSubnetCidr):  # String
		self.add_query_param('FirewallSubnetCidr', FirewallSubnetCidr)
	def get_FirewallDescription(self): # String
		return self.get_query_params().get('FirewallDescription')

	def set_FirewallDescription(self, FirewallDescription):  # String
		self.add_query_param('FirewallDescription', FirewallDescription)
	def get_RouteMode(self): # String
		return self.get_query_params().get('RouteMode')

	def set_RouteMode(self, RouteMode):  # String
		self.add_query_param('RouteMode', RouteMode)
	def get_TrAttachmentMasterCidr(self): # String
		return self.get_query_params().get('TrAttachmentMasterCidr')

	def set_TrAttachmentMasterCidr(self, TrAttachmentMasterCidr):  # String
		self.add_query_param('TrAttachmentMasterCidr', TrAttachmentMasterCidr)
	def get_FirewallVpcId(self): # String
		return self.get_query_params().get('FirewallVpcId')

	def set_FirewallVpcId(self, FirewallVpcId):  # String
		self.add_query_param('FirewallVpcId', FirewallVpcId)
	def get_FirewallName(self): # String
		return self.get_query_params().get('FirewallName')

	def set_FirewallName(self, FirewallName):  # String
		self.add_query_param('FirewallName', FirewallName)
	def get_TransitRouterId(self): # String
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self, TransitRouterId):  # String
		self.add_query_param('TransitRouterId', TransitRouterId)
	def get_FirewallVpcCidr(self): # String
		return self.get_query_params().get('FirewallVpcCidr')

	def set_FirewallVpcCidr(self, FirewallVpcCidr):  # String
		self.add_query_param('FirewallVpcCidr', FirewallVpcCidr)
	def get_RegionNo(self): # String
		return self.get_query_params().get('RegionNo')

	def set_RegionNo(self, RegionNo):  # String
		self.add_query_param('RegionNo', RegionNo)
	def get_TrAttachmentSlaveCidr(self): # String
		return self.get_query_params().get('TrAttachmentSlaveCidr')

	def set_TrAttachmentSlaveCidr(self, TrAttachmentSlaveCidr):  # String
		self.add_query_param('TrAttachmentSlaveCidr', TrAttachmentSlaveCidr)
