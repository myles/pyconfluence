import xmlrpclib

from pyconfluence.exceptions import NotImplementedException

class BaseResponse(object):
	"""
	The base class for the XML-RPC Response.
	"""
	def __repr(self):
		return "<<%s>>" % str(self.__class__)

class ServerInfo(BaseResponse):
	"""
	:param major_version: the major version number of the Confluence instance
	:type major_version: int
	:param minor_version: the minor version number of the Confluence instance
	:type minor_version: int
	:param patch_level: the patch-level of the Confluence instance
	:type patch_level: int
	:param build_id: the build ID of the Confluence instance (usually a number)
	:type build_id: str
	:param development_build: whether the build is a developer-only release or not
	:type development_build: bool
	:param base_url: the base URL for the confluence instance
	:type base_url: str
	"""
	def __init__(self):
		self.major_version = 0
		self.minor_version = 0
		self.patch_level = 0
		self.build_id = ''
		self.development_build = False
		self.base_url = ''
	
	def display(self, server_info):
		"""Convert the XML-RPC varables to ServerInfo class.
		
		:param server_info: The XML-RPC dict
		:type server_info: dict
		"""
		self.major_version = int(server_info['majorVersion'])
		self.minor_version = int(server_info['minorVersion'])
		self.patch_level = int(server_info['patchLevel'])
		self.build_id = str(server_info['buildId'])
		if server_info['developmentBuild'] == 'false':
			self.development_build = False
		elif server_info['developmentBuild'] == 'true':
			self.development_build = True
		self.base_url = str(server_info['baseUrl'])
		return self

class SpaceSummary(BaseResponse):
	"""
	:param key: the space key
	:type key: str
	:param name: the name of the space
	:type key: str
	:param type: type of the space
	:type type: str
	:param url: the url to the view this space online
	:type url: str
	"""
	def __init__(self):
		self.key = ''
		self.name = ''
		self.type = ''
		self.url = ''
	
	def display(self, space_summary):
		"""Convert the XML-RPC dict to the SpaceSummary class.
		
		:param space_summary: The XML-RPC dict
		:type space_summary: dict
		"""
		self.key = str(space_summary['key'])
		self.name = str(space_summary['name'])
		self.type = str(space_summary['type'])
		self.url = str(space_summary['url'])
		return self

class Space(BaseResponse):
	"""
	:param key: the space key
	:type key: str
	:param name: the name of the space
	:type name: str
	:param url: the url to view this space online
	:type url: str
	:param homepage: the id of the space homepage
	:type homepage: str
	:param description: the HTML rendered space description
	:type description: str
	"""
	def __init__(self):
		self.key = ''
		self.name = ''
		self.url = ''
		self.homepage = ''
		self.description = ''

class PageSummary(BaseResponse):
	"""
	:param id: the id of the page
	:type id: str
	:param space: the key of the space taht this page belongs to
	:type space: str
	:param parent_id: the id of the parent page
	:type parent_id: str
	:param title: the title of the page
	:type title: str
	:param url: the url to view this page online
	:type url: str
	:param locks: the number of locks current on this page
	:type locks: int
	"""
	def __init__(self):
		self.id = ''
		self.space = ''
		self.parent_id = ''
		self.title = ''
		self.url = ''
		self.locks = 0

class Confluence(object):
	"""
	:param url: the URL to the confluence wiki.
	:param username: if not provide will login as an anonymous user.
	:param password: if not provide will login as an anonymous user.
	"""
	def __init__(self, url, username=None, password=None):
		self.url = url
		self.server = xmlrpclib.ServerProxy("%s%s" % (self.url, '/rpc/xmlrpc'))
		self.token = self.login(username, password)
	
	# *-* Authentication Methods *-*
	
	@property
	def login(self, username=None, password=None):
		"""Log a user into Confluence and returns a token. if the username
		and password is not provided will login as an anonymous user.
		
		:param username: if not provide will login as an anonymous user.
		:type username: str or None
		:param password: if not provide will login as an anonymous user.
		:type username: str or None
		:return: logged in token.
		:rtype: str
		"""
		if username and password:
			token = self.server.confluence1.login(username, password)
		else:
			token = None
		return token
	
	@property
	def logout(self):
		"""Removes the token from the list of logged in tokes.
		
		:return: if True the user has been logged out, if False the user was never logged in.
		:rtype: bool
		"""
		return self.server.confluence1.logout(self.token)
	
	# -*- Administration -*-
	
	@property
	def export_site(self, export_attachments):
		"""Exports a confluence instance.
		
		:param export_attachments: should attachments be include
		:type export_attachments: bool
		:return: URL to the exported file.
		:rtype: str
		"""
		return self.server.confluence1.exportSite(self.token, export_attchments)
	
	@property
	def get_cluster_information(self):
		"""Returns information about the cluster this node is part of.
		
		:returns: ClusterInformation
		"""
		raise NotImplementedException
	
	@property
	def get_cluster_node_statuses(self):
		"""Returns the status of all nodes in the cluster.
		
		:returns: list of NodeStatus
		:rtype: list
		"""
		raise NotImplementedException
	
	# -*- General -*-
	
	@property
	def get_server_info(self):
		"""Retrieve some basic information about the server connected to.
		
		:returns: ServerInfo
		"""
		try:
			response = self.server.confluence1.getServerInfo(self.token)
			server_info = ServerInfo().display(response)
			return server_info
		except xmlrpclib.Fault, fault:
			raise fault
	
	# -*- Spaces Retrieval *-*
	
	@property
	def get_spaces(self):
		"""All Space Summaries that the current user can see.
		
		:returns: SpaceSummary
		:rtype: list
		"""
		raise NotImplementedException
	
	@property
	def get_space(self):
		"""Returns a signle space.
		
		:returns: Space
		"""
		raise NotImplementedException
	
	@property
	def export_space(self, space_key, export_type='TYPE_XML'):
		"""Export a space and returns a URL for download. You can provide
		an export type `TYPE_XML`, `TYPE_PDF`, or `TYPE_HTML`. The default
		is `TYPE_XML`.
		
		:param space_key:
		:type space_key: str
		:param export_type: the type of format that you would like to export.
		:type export_type: str
		"""
		raise NotImplementedException
	
	# -*- Spaces Management *-*
	
	@property
	def add_space(self, space):
		"""Create a new space.
		
		:param space: a Space object.
		:type space: Space
		
		:returns: Space
		"""
		raise NotImplementedException
	
	@property
	def remove_space(self, space_key):
		"""Removes a space completely.
		
		:param space_key:
		:type space_key: str
		
		:returns: True if was successful.
		:rtype: bool
		"""
		raise NotImplementedException
	
	@property
	def add_personal_space(self, personal_space, user_name):
		"""Add a new space as a personal space.
		
		:param personal_space: a Space object.
		:type personal_space: Space
		:param user_name: the user you would like to add the personal space to.
		:type user_name: str
		
		:returns: Space
		"""
		raise NotImplementedException
	
	@property
	def convert_to_personal_space(self, user_name, space_key, new_space_name, update_links=True):
		"""Convert an existing space to a personal space.
		
		:param user_name:
		:type user_name: str
		:param space_key:
		:type space_key: str
		:param new_space_name:
		:type new_space_name: str
		:param update_links: update the links in other spaces to point to the new space. Defaults to True.
		:type update_links: bool
		"""
		try:
			response = self.server.confluence1.convertToPersonalSpace(self.token, user_name, space_key, new_space_name, update_links)
			if response == 'true':
				return True
			elif response == 'false':
				return False
		except xmlrpclib.Fault, fault:
			raise fault