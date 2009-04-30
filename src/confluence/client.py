import xmlrpclib

class ServerInfo:
	def __init__(self):
		self.major_version = 0
		self.minor_version = 0
		self.patch_level = 0
		self.build_id = ''
		self.development_build = False
		self.base_url = ''

class Confluence:
	def __init__(self, url, username=None, password=None):
		self.url = url
		self.server = xmlrpclib.ServerProxy("%s%s" % (self.url, '/rpc/xmlrpc'))
		self.token = self.login(username, password)
		
	def _filter_server_info(self, server_info):
		obj = ServerInfo()
		obj.major_version = int(server_info['majorVersion'])
		obj.minor_version = int(server_info['minorVersion'])
		obj.patch_level = int(server_info['patchLevel'])
		obj.build_id = server_info['buildId']
		if server_info['developmentBuild'] == 'false':
			obj.development_build = False
		elif server_info['developmentBuild'] == 'true':
			obj.development_build = True
		obj.base_url = server_info['baseUrl']
		return obj
	
	def login(self, username=None, password=None):
		"""
		log in a user. Returns a String authentication token to be passed
		as authentication to all other remote calls.
		From 1.3 onwards, you can supply an empty string as the token to
		be treated as being the anonymous user.
		"""
		if username and password:
			token = self.server.confluence1.login(username, password)
		else:
			token = None
		return token
	
	def logout(self):
		"""
		remove this token from the list of logged in tokens.Returns true
		if the user was logged out, false if they were not logged in in
		the first place.
		"""
		return self.server.confluence1.logout(self.token)
	
	def export_site(self, export_attachments):
		"""
		exports a Confluence instance and returns a String holding the URL
		for the download. The boolean argument indicates whether or not
		attachments ought to be included in the export.
		"""
		return self.server.confluence1.exportSite(self.token, export_attchments)
	
	def get_server_info(self):
		"""
		retrieve some basic information about the server being connected to.
		Useful for clients that need to turn certain features on or off
		depending on the version of the server. (Since 1.0.3)
		"""
		try:
			response = self.server.confluence1.getServerInfo(self.token)
			server_info = self._filter_server_info(response)
			return server_info
		except xmlrpclib.Fault, fault:
			raise fault
