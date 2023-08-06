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

class AddAddressBookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudfw', '2017-12-07', 'AddAddressBook','cloudfirewall')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_TagLists(self): # RepeatList
		return self.get_query_params().get('TagList')

	def set_TagLists(self, TagList):  # RepeatList
		for depth1 in range(len(TagList)):
			if TagList[depth1].get('TagValue') is not None:
				self.add_query_param('TagList.' + str(depth1 + 1) + '.TagValue', TagList[depth1].get('TagValue'))
			if TagList[depth1].get('TagKey') is not None:
				self.add_query_param('TagList.' + str(depth1 + 1) + '.TagKey', TagList[depth1].get('TagKey'))
	def get_GroupType(self): # String
		return self.get_query_params().get('GroupType')

	def set_GroupType(self, GroupType):  # String
		self.add_query_param('GroupType', GroupType)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_AutoAddTagEcs(self): # String
		return self.get_query_params().get('AutoAddTagEcs')

	def set_AutoAddTagEcs(self, AutoAddTagEcs):  # String
		self.add_query_param('AutoAddTagEcs', AutoAddTagEcs)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_AddressList(self): # String
		return self.get_query_params().get('AddressList')

	def set_AddressList(self, AddressList):  # String
		self.add_query_param('AddressList', AddressList)
	def get_TagRelation(self): # String
		return self.get_query_params().get('TagRelation')

	def set_TagRelation(self, TagRelation):  # String
		self.add_query_param('TagRelation', TagRelation)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
