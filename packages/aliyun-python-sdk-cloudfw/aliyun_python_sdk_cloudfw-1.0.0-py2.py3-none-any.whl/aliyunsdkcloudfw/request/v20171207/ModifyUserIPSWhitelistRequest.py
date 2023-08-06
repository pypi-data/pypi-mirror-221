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

class ModifyUserIPSWhitelistRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'ModifyUserIPSWhitelist','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WhiteType(self): # Long
		return self.get_query_params().get('WhiteType')

	def set_WhiteType(self, WhiteType):  # Long
		self.add_query_param('WhiteType', WhiteType)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_ListValue(self): # String
		return self.get_query_params().get('ListValue')

	def set_ListValue(self, ListValue):  # String
		self.add_query_param('ListValue', ListValue)
	def get_ListType(self): # Long
		return self.get_query_params().get('ListType')

	def set_ListType(self, ListType):  # Long
		self.add_query_param('ListType', ListType)
	def get_IpVersion(self): # String
		return self.get_query_params().get('IpVersion')

	def set_IpVersion(self, IpVersion):  # String
		self.add_query_param('IpVersion', IpVersion)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Direction(self): # Long
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # Long
		self.add_query_param('Direction', Direction)
