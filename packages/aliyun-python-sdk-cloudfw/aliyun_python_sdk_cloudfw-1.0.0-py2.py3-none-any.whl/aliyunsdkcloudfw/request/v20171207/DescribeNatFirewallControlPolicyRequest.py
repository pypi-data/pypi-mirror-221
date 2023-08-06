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

class DescribeNatFirewallControlPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'DescribeNatFirewallControlPolicy','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Release(self): # String
		return self.get_query_params().get('Release')

	def set_Release(self, Release):  # String
		self.add_query_param('Release', Release)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_AclUuid(self): # String
		return self.get_query_params().get('AclUuid')

	def set_AclUuid(self, AclUuid):  # String
		self.add_query_param('AclUuid', AclUuid)
	def get_AclAction(self): # String
		return self.get_query_params().get('AclAction')

	def set_AclAction(self, AclAction):  # String
		self.add_query_param('AclAction', AclAction)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_CurrentPage(self): # String
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # String
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Proto(self): # String
		return self.get_query_params().get('Proto')

	def set_Proto(self, Proto):  # String
		self.add_query_param('Proto', Proto)
