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

class CreateNatFirewallControlPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'CreateNatFirewallControlPolicy','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DestPortType(self): # String
		return self.get_query_params().get('DestPortType')

	def set_DestPortType(self, DestPortType):  # String
		self.add_query_param('DestPortType', DestPortType)
	def get_Release(self): # String
		return self.get_query_params().get('Release')

	def set_Release(self, Release):  # String
		self.add_query_param('Release', Release)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_DestPortGroup(self): # String
		return self.get_query_params().get('DestPortGroup')

	def set_DestPortGroup(self, DestPortGroup):  # String
		self.add_query_param('DestPortGroup', DestPortGroup)
	def get_ApplicationNameLists(self): # RepeatList
		return self.get_query_params().get('ApplicationNameList')

	def set_ApplicationNameLists(self, ApplicationNameList):  # RepeatList
		for depth1 in range(len(ApplicationNameList)):
			self.add_query_param('ApplicationNameList.' + str(depth1 + 1), ApplicationNameList[depth1])
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_AclAction(self): # String
		return self.get_query_params().get('AclAction')

	def set_AclAction(self, AclAction):  # String
		self.add_query_param('AclAction', AclAction)
	def get_NewOrder(self): # String
		return self.get_query_params().get('NewOrder')

	def set_NewOrder(self, NewOrder):  # String
		self.add_query_param('NewOrder', NewOrder)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_IpVersion(self): # String
		return self.get_query_params().get('IpVersion')

	def set_IpVersion(self, IpVersion):  # String
		self.add_query_param('IpVersion', IpVersion)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_DomainResolveType(self): # Integer
		return self.get_query_params().get('DomainResolveType')

	def set_DomainResolveType(self, DomainResolveType):  # Integer
		self.add_query_param('DomainResolveType', DomainResolveType)
	def get_Proto(self): # String
		return self.get_query_params().get('Proto')

	def set_Proto(self, Proto):  # String
		self.add_query_param('Proto', Proto)
	def get_DestPort(self): # String
		return self.get_query_params().get('DestPort')

	def set_DestPort(self, DestPort):  # String
		self.add_query_param('DestPort', DestPort)
