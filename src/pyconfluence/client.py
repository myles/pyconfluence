import xmlrpclib

from pyconfluence.exceptions import NotImplementedException

class ServerInfo(object):
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
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.base_url)
	
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

class SpaceSummary(object):
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
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.key)
	
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

class Space(object):
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
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.key)
	
	def display(self, space):
		"""Convert the XML-RPC dict to the Space class.
		
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.key = str(space['key'])
		self.name = str(space['name'])
		self.type = str(space['type'])
		self.url = str(space['url'])
		self.homepage = str(space['homepage'])
		self.description = str(space['description'])
		return self

class PageSummary(object):
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
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.id)
	
	def display(self, page_summary):
		"""Convert the XML-RPC dict to the PageSummary class.
		
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(page_summary['id'])
		self.parent_id = str(page_summary['parent_id'])
		self.title = str(page_summary['title'])
		self.url = str(page_summary['url'])
		self.locks = int(page_summary['locks'])
		return self

class Page(object):
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
	:param version: the version number of this page
	:type version: int
	:param content: the page content
	:type content: str
	:param created: timestamp page was created
	:type created: datetime
	:param creator: username of the creator
	:type creator: str
	:param modified: timestamp page was modified
	:type modified: str
	:param modifier: username of page's last modifier
	:type modifier: str
	:param home_page: whether or not his is a space's homepage
	:type home_page: bool
	:param locks: the number of locks current on this page
	:type locks: int
	:param content_status: status of the page (eg. current or deleted)
	:type cotnent_status: str
	:param current: whether the page is current and not deleted
	:type current: bool
	"""
	
	def __init__(self):
		self.id = ''
		self.space = ''
		self.parent_id = ''
		self.title = ''
		self.url = ''
		self.version = ''
		self.content = ''
		self.created = ''
		self.creator = ''
		self.modified = ''
		self.modifier = ''
		self.homepage = ''
		self.lock = 0
		self.content_status = ''
		self.current = ''
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.id)

class PageHistorySummary(object):
	"""
	:param id: the id of the historical page
	:type id: str
	:param version: the version of the historical page
	:type versoin: int
	:param modifier: the user who made the change
	:type modifier: str
	:param modified: timestamp change was made
	:type modified: datetime
	:param version_comment: the comment made when the version was changed
	:type version_comment: str
	"""

class BlogEntrySummary(object):
	"""
	:param id: the id of the blog entry
	:type id: str
	:param space: the key of the space that this blog entry belongs to
	:type space: str
	:param title: the title of the blog entry
	:type title: str
	:param url: the url to view this blog entry online
	:type url: str
	:param locks: the number of locks current on this page
	:type locks: int
	:param publish_date: the date the blog post was published
	:type published_date: datetime
	"""

class BlogEntrySummary(object):
	"""
	:param id: the id of the blog entry
	:type id: str
	:param space: the key of the space that this blog entry belongs to
	:type space: str
	:param title: the title of the blog entry
	:type title: str
	:param url: the url to view this blog entry online
	:type url: str
	:param url: the url to view this blog entry online
	:type url: str
	:param content: the blog entry content
	:type content: str
	:param locks: the number of locks current on this page
	:type locks: int
	"""

class RSSFeed(object):
	"""
	:param url: the URL of the RSS feed
	:type url: str
	:param title: the feed's title
	:type title: str
	"""

class SearchResult(object):
	"""
	:param title: the feed's title
	:type title: str
	:param url: the remote URL needed to view the search result online
	:type url: str
	:param excerpt: a short excerpt of the result if it makes sense
	:type excerpt: str
	:param content_type: the type of this result - page, comment, spacedesc, attachment, userinfo, blogpost
	:type content_type: str
	:param id: the long ID of the result (if the type has one)
	:type id: str
	"""

class Attachment(object):
	"""
	:param id: numeric id of the attachment
	:type id: int
	:param page_id: page ID of the attachment
	:type page_id: str
	:param title: title of the attachment
	:type title: str
	"""

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
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.url)
	
	# *-* Authentication Methods *-*
	
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
	
	def logout(self):
		"""Removes the token from the list of logged in tokes.
		
		:return: if True the user has been logged out, if False the user was never logged in.
		:rtype: bool
		"""
		return self.server.confluence1.logout(self.token)
	
	# -*- Administration -*-
	
	def export_site(self, export_attachments):
		"""Exports a confluence instance.
		
		:param export_attachments: should attachments be include
		:type export_attachments: bool
		:return: URL to the exported file.
		:rtype: str
		"""
		return self.server.confluence1.exportSite(self.token, export_attchments)
	
	def get_cluster_information(self):
		"""Returns information about the cluster this node is part of.
		
		:returns: ClusterInformation
		"""
		raise NotImplementedException
	
	def get_cluster_node_statuses(self):
		"""Returns the status of all nodes in the cluster.
		
		:returns: list of NodeStatus
		:rtype: list
		"""
		raise NotImplementedException
	
	# -*- General -*-
	
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
	
	def get_spaces(self):
		"""All Space Summaries that the current user can see.
		
		:returns: SpaceSummary
		:rtype: list
		"""
		raise NotImplementedException
	
	def get_space(self):
		"""Returns a signle space.
		
		:returns: Space
		"""
		raise NotImplementedException
	
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
	
	def add_space(self, space):
		"""Create a new space.
		
		:param space: a Space object.
		:type space: Space
		
		:returns: Space
		"""
		raise NotImplementedException
	
	def remove_space(self, space_key):
		"""Removes a space completely.
		
		:param space_key:
		:type space_key: str
		
		:returns: True if was successful.
		:rtype: bool
		"""
		raise NotImplementedException
	
	def add_personal_space(self, personal_space, user_name):
		"""Add a new space as a personal space.
		
		:param personal_space: a Space object.
		:type personal_space: Space
		:param user_name: the user you would like to add the personal space to.
		:type user_name: str
		
		:returns: Space
		"""
		raise NotImplementedException
	
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
