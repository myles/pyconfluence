import xmlrpclib

class NotImplementedException(Exception):
	pass

class ConfluenceException(Exception):
	pass

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
	
	def __str__(self):
		return "Atlassian Confluence %s" % (self.version)
	
	def __unicode__(self):
		return unicode(__str__)
	
	@property
	def version(self):
		return ".".join(map(str, (self.major_version,
			self.minor_version, self.patch_level)))
		
	
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
	
	def __str__(self):
		return "%s" % (self.name)
	
	def __unicode__(self):
		return unicode(__str__)
	
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
	
	def __str__(self):
		return "%s" % (self.name)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, space):
		"""Convert the XML-RPC dict to the Space class.
		
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.key = str(space['key'])
		self.name = str(space['name'])
		self.type = str(space['type'])
		self.url = str(space['url'])
		self.homepage = str(space['homePage'])
		try:
			self.description = str(space['description'])
		except KeyError:
			self.description = None
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
	
	def __str__(self):
		return "%s" % (self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, page_summary):
		"""Convert the XML-RPC dict to the PageSummary class.
		
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(page_summary['id'])
		try:
			self.parent_id = str(page_summary['parent_id'])
		except KeyError:
			self.parent_id = None
		self.title = str(page_summary['title'])
		self.url = str(page_summary['url'])
		try:
			self.locks = int(page_summary['locks'])
		except KeyError:
			self.locks = None
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
	
	def __str__(self):
		return "%s" % (self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, page):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(page['id'])
		self.space = str(page['space'])
		self.parent_id = str(page['parent_id'])
		self.title = str(page['title'])
		self.url = str(page['url'])
		self.version = int(page['version'])
		self.content = str(page['content'])
		self.created = str(page['created'])
		self.creator = str(page['creator'])
		self.modified = str(page['modified']) # TODO Convert to datetime object.
		self.modifier = str(page['modifier'])
		self.homepage = bool(page['homepage'])
		self.lock = int(page['locks'])
		self.content_status = str(page['content_status'])
		self.current = bool(page['current'])
		return self

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
	
	def __init__(self):
		self.id = ''
		self.version = 0
		self.modifier = ''
		self.modified = ''
		self.version_comment = ''
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.id)
	
	def __str__(self):
		return "%s" % (self.id)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, page):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(page['id'])
		self.version = int(page['version'])
		self.modifier = str(page['modifier'])
		self.modified = page['modified'] # TODO Convert to datetime object.
		try:
			self.version_comment = str(page['versionComment'])
		except KeyError:
			self.version_comment = ''
		return self

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
	:type publish_date: datetime
	"""
	
	def __init__(self):
		self.id = ''
		self.space = ''
		self.title = ''
		self.url = ''
		self.locks = 0
		self.publish_date = ''
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.id)
	
	def __str__(self):
		return "[%s] %s" % (self.space, self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, entry):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(entry['id'])
		self.space = str(entry['space'])
		self.title = str(entry['title'])
		self.url = str(entry['url'])
		self.locks = int(entry['locks'])
		self.publish_date = entry['publishDate'] # TODO Convert to datetime object.
		return self

class BlogEntry(object):
	"""
	:param id: the id of the blog entry
	:type id: str
	:param space: the key of the space that this blog entry belongs to
	:type space: str
	:param title: the title of the blog entry
	:type title: str
	:param url: the url to view this blog entry online
	:type url: str
	:param version: the version number of this blog entry
	:type version: int
	:param content: the blog entry content
	:type content: str
	:param locks: the number of locks current on this page
	:type locks: int
	"""
	
	def __init__(self):
		self.id = ''
		self.space = ''
		self.title = ''
		self.url = ''
		self.version = 0
		self.content = ''
		self.locks = 0
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.id)
	
	def __str__(self):
		return "[%s] %s" % (self.space, self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, entry):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.id = str(entry['id'])
		self.space = str(entry['space'])
		self.title = str(entry['title'])
		self.url = str(entry['url'])
		self.version = int(entry['version'])
		self.content = str(entry['content'])
		self.locks = int(entry['locks'])
		return self

class RSSFeed(object):
	"""
	:param url: the URL of the RSS feed
	:type url: str
	:param title: the feed's title
	:type title: str
	"""
	
	def __init__(self):
		self.url = url
		self.title = title
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.title)
	
	def __str__(self):
		return "%s" % (self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, feed):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.url = str(feed['url'])
		self.title = str(feed['title'])
		return self

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
	
	def __init__(self):
		self.title = ''
		self.url = ''
		self.excerpt = ''
		self.type = ''
		self.id = ''
	
	def __repr__(self):
		return '<%s %r>' % (type(self).__name__, self.title)
	
	def __str__(self):
		return "%s" % (self.title)
	
	def __unicode__(self):
		return unicode(__str__)
	
	def display(self, result):
		"""Convert the XML-RPC dict to the Page class.
	
		:param space: The XML-RPC dict
		:type space: dict
		"""
		self.title = str(result['title'])
		self.url = str(result['url'])
		self.excerpt = str(result['excerpt'])
		self.type = str(result['type'])
		self.id = str(result['id'])
		return self

class Attachment(object):
	"""
	:param id: numeric id of the attachment
	:type id: int
	:param page_id: page ID of the attachment
	:type page_id: str
	:param title: title of the attachment
	:type title: str
	:param file_name: file name of the attachment
	:type file_name: str
	:param file_size: numeric file size of the attachment in bytes
	:type file_size: str
	:param content_type: mime content type of the attachment
	:param created: creation date of the attachment
	:type created: datetime
	:param creator: creator of the attachment
	:type creator: str
	:param url: url to download the attachment online
	:type url: str
	:param comment: comment for the attachment
	:type comment: str
	"""

class Comment(object):
	"""
	:param id: numeric id of the comment
	:type id: str
	:param page_id: page ID of the comment
	:type page_id: str
	:param title: title of the comment
	:param content: notated content of the comment (use render_content to render)
	:type content: str
	:param url: url to view the comment online
	:type url: str
	:param created: creation date of the comment
	:type created: datetime
	:param creator: creator of the attachment
	:type creator: str
	"""

class User(object):
	"""
	:param name: the username of this user
	:type name: str
	:param fullname: the full name of this user
	:type fullname: str
	:param email: the email address of this user
	:type email: str
	:param url: the url to view this user online
	:type url: str
	"""

class ContentPermission(object):
	"""
	:param content_type: the type of permission. One of 'View' or 'Edit'
	:type content_type: str
	:param user_name: the username of the user who is permitted to see or edit the content. 'None' if this is a group permission.
	:type user_name: str
	:param group_name: The name of the group who is permitted to see or edit the content. 'None' if this is a user permission.
	:type group_name: str
	"""

class Label(object):
	"""
	:param name: the name of the label
	:type name: str
	:param owner: the username of the owner
	:type owner: str
	:param namespace: the namespace of the label
	:type namespace: str
	:param id: the ID of the label
	:type id: int
	"""

class UserInformation(object):
	"""
	:param username: the username of this user
	:type username: str
	:param content: the user description
	:type content: str
	:param creator_name: the creator of the user
	:type creator_name: str
	:param last_modifier_name: the user who last modified
	:type last_modifier_name: str
	:param url: the url to view this user online
	:type url: type
	:param version: the version
	:type version: int
	:param id: the ID of the user
	:type id: int
	:param creation_date: the date the user was created
	:type creation_date: datetime
	:param last_modification_date: the date the user was last modified
	:type last_modification_date: datetime
	"""

class ClusterInformation(object):
	"""
	:param is_running: true if this node is part of a cluster
	:type is_running: bool
	:param name: the name of the cluster
	:type name: str
	:param member_count: the number of nodes in hte cluster, including this node (this will be zero if this node is not clustered)
	:type member_count: int
	:param description: a description of the cluster
	:type description: str
	:param multicast_address: the address that this cluster uses for multicast communication
	:type multicast_address: str
	:param multicast_port: the port that this cluster uses for multicast communication
	:type multicast_port: int
	"""

class NodeStat(object):
	"""
	:param node_id: an integer uniquely idetifying the node within the cluster
	:type node_id: int
	:param jvm_status: a dict containing attributes about the JVM memory usage of node. Keys are "total.memory", "free.memory", "used.memory"
	:type jvm_status: dict
	:param props: a dict containing attributes of the node Keys are "system.date", "system.time", "system.favourite.colour", "java.version", "java.vendor", "jvm.version", "jvm.vendeor", "jvm.implemtation.version", "java.runtime", "java.vm", "user.name.word", "user.timezone", "operating.system", "os.architecture", "fs.encoding"
	:type props: dict
	:param build_stats: a dict containing attributes of the build of Confluence running on the node. Kyes are "confluence.home", "system.uptime", "system.version", "build.number"
	:type build_status: dict
	"""

class Confluence(object):
	"""
	:param url: the URL to the confluence wiki.
	:param username: if not provide will login as an anonymous user.
	:param password: if not provide will login as an anonymous user.
	"""
	def __init__(self, url, username=None, password=None):
		self.url = url
		self.server = xmlrpclib.ServerProxy("%s%s" % (self.url, '/rpc/xmlrpc'),
			allow_none=True)
		if username and password:
			self.token = self.login(username, password)
		else:
			self.token = None
	
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
			try:
				token = self.server.confluence1.login(username, password)
			except xmlrpclib.Fault, fault:
				raise ConfluenceException(fault.faultString)
			except xmlrpclib.ProtocolError, err:
				raise ConfluenceException(err.url, err.errmsg)
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
	
	def is_plugin_enabled(self, plugin_key):
		"""Returns true if the plugin is installed and enabled,
		otherwise false.
		
		:param plugin_key:
		:type plugin_key: str
		:returns:
		:rtype: bool
		"""
		try:
			response = self.server.confluence1.isPluginEnabled(self.token, plugin_key)
			return response
		except xmlrpclib.Fault, fault:
			raise ConfluenceException(fault.faultString)
	
	def install_plugin(self):
		"""Installs a plugin in Confluence. Returns false if the file
		is not a JAR or XML file. Throws an exception if the
		installation fails for another reason.
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
			raise ConfluenceException(fault.faultString)
	
	# -*- Spaces Retrieval *-*
	
	def get_spaces(self):
		"""All Space Summaries that the current user can see.
		
		:returns: SpaceSummary
		:rtype: list
		"""
		try:
			responses = self.server.confluence1.getSpaces(self.token)
			spaces = []
			for response in responses:
				spaces += [SpaceSummary().display(response),]
			return spaces
		except xmlrpclib.Fault, fault:
			raise ConfluenceException(fault.faultString)
	
	def get_space(self, key):
		"""Returns a signle space.
		
		:param key: The key to the space.
		:type key: str
		:returns: Space
		"""
		try:
			response = self.server.confluence1.getSpace(self.token, key)
			space = Space().display(response)
			return space
		except xmlrpclib.Fault, fault:
			raise ConfluenceException(fault.faultString)
	
	def export_space(self, space_key, export_type='TYPE_XML'):
		"""Export a space and returns a URL for download. You can provide
		an export type `TYPE_XML`, or `TYPE_HTML`. The default is `TYPE_XML`.
		
		:param space_key:
		:type space_key: str
		:param export_type: the type of format that you would like to export.
		:type export_type: str
		
		:returns: str
		"""
		try:
			response = self.server.confluence1.exportSpace(self.token, space_key, export_type)
			return response
		except xmlrpclib.Fault, fault:
			raise fault
	
	def export_space_pdf(self, space_key):
		try:
			response = self.server.pdfexport.confluence1.exportSpace(self.token, space_key)
			return response
		except xmlrpclib.Fault, fault:
			raise fault
	
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
	
	def store_space(self, space):
		"""Create a new space if passing in a name, key and description *or* update
		the properties of an existing space. Only name, homepage or space group can
		be changed.
		
		:param space: 
		:type space: Space
		
		:returns: Space
		"""
		raise NotImplementedException
	
	def import_space(self, data):
		"""Import a space into Confluence. *Note that this uses a lot
		of memory - about 4 times the size of the upload*. The data
		provided should be a zipped XML backup, the same as exported
		by Confluence.
		
		:param data: A zipped XML backup.
		:type data: byte
		:rtype: bool
		"""
		raise NotImplementedException
	
	# -*- Pages Retrieval *-*
	
	def get_pages(self, space_key):
		"""Returns all the PageSummaries in the space. Doesn't
		include pages which are in the Trash.
		
		:parma space_key:
		:type space_key: str:
		:rtype: list
		"""
		try:
			responses = self.server.confluence1.getPages(self.token, space_key)
			pages = []
			for response in responses:
				pages += [PageSummary().display(response),]
			return pages
		except xmlrpclib.Fault, fault:
			raise fault
	
	def get_page(self, page_id):
		"""Returns a single Page
		
		:param page_id:
		:type page_id: str
		:rtype: Page
		"""
		
		raise NotImplementedException
	
	def get_page_title(self, page_title, space_key):
		"""Returns a single Page
		
		:param space_key:
		:type space_key: str
		:rtype: Page
		"""
		
		raise NotImplementedException
	
	def get_page_history(self, page_id):
		"""Returns all the PageHistorySummaries - useful for looking
		up the previous versions of a page, and who changed them.
		
		:param page_id:
		:type page_id:
		:rtype: list
		"""
		
		try:
			responses = self.server.confluence1.getPageHistory(self.token, page_id)
			history = []
			for response in responses:
				history += [PageHistorySummary().display(response),]
			return history
		except xmlrpclib.Fault, fault:
			raise fault
	
	# -*- Pages Management *-*
	
	# -*- Attachments Retrieval *-*
	# -*- Attachments Management *-*
	
	# -*- Blog Entries *-*
	
	# -*- Search *-*
	
	def search(self, query, max_results=20, space_key=None, content_type=None,
			modified=None, contributor=None):
		"""Return a list of SearchResults which match a given search query (including
		page and other content types).
		
		:param query:
		:type query: str
		:param max_results:
		:type max_results: int
		:param space_key:
		:type space_key: str
		:param content_type:
		:type content_type: str
		:param modified:
		:type modified: str
		:param contributor:
		:type space_key: str
		
		:returns: dict
		"""
		parameters = {}
		if space_key:
			parameters['spaceKey'] = space_key
		elif content_type:
			parameters['type'] = content_type
		elif modified:
			parameters['modified'] = modified
		elif contributor:
			parameters['contributor']
		else:
			parameters = None
		
		try:
			if not parameters:
				response = self.server.confluence1.search(self.token, query, parameters,
					max_results)
			else:
				response = self.server.confluence1.search(self.token, query, max_results)
			
			results = []
			for r in respone:
				results += [SearchResult(r)]
			
			return results
		except xmlrpclib.Fault, fault:
			raise fault
	
	# -*- Security Retrieval *-*
	
	# -*- User Management *-*
	
	# -*- Labels *-*