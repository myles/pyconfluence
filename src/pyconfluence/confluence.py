import os
import logging
import ConfigParser
from optparse import OptionParser

from pyconfluence import __version__, Confluence, ConfluenceException

USAGE = """%prog [options]

get_server_info:\t Retrieve some basic information about the server connected to.
get_spaces:\t\t All Space Summaries that the current user can see.
get_space:\t\t Returns a signle space."""

SPACE_NOT_FOUND_OR_AUTH = "You are not allowed to view %(key)s space, or it doesn't exist."

def main():
	parser = OptionParser(usage=USAGE, version=__version__)
	parser.add_option('-c', '--confluence', action='store', dest='confluence_url',
		help="the confluence url.")
	parser.add_option('-u', '--username', action='store', dest='username',
		help="the username to use for authentication.")
	parser.add_option('-p', '--password', action='store', dest='password',
		help="the password to use for authentication.")
	parser.add_option('-v', '--verbosity', action='store', dest='verbosity',
		default='1', type='choice', choices=['0', '1', '2'],
		help='Verbosity level; 0=minimal output, 1=normal output, 2=all output')
	parser.set_defaults(input='-')
	
	options, args = parser.parse_args()
	
	level = {'0': logging.WARN, '1': logging.INFO, '2': logging.DEBUG}[options.verbosity]
	logging.basicConfig(level=level, format="%(name)s: %(levelname)s: %(message)s")
	log = logging.getLogger('pyconfluence')
	
	if not args:
		log.warn("You didn't tell me anything.") # FIXME
		return
	
	config = ConfigParser.ConfigParser()
	config.read(os.path.expanduser("~/.pyconfluence.ini"))
	
	confluence_url = options.confluence_url
	username = options.username
	password = options.password
	
	if config.get('pyconfluence', 'url'):
		confluence_url = config.get('pyconfluence', 'url')
	
	if config.get('pyconfluence', 'username'):
		username = config.get('pyconfluence', 'username')
	
	if config.get('pyconfluence', 'password'):
		password = config.get('pyconfluence', 'password')
	
	try:
		c = Confluence(confluence_url, username, password)
	except ConfluenceException, err:
		log.warn("Their was an error connecting to the server %(url)s using the username %(username)s.\n%(err)s" % {'url': confluence_url, 'username': username, 'err': err})
	
	if args[0] == 'get_server_info':
		print c.get_server_info()
	if args[0] == 'get_spaces':
		for space in c.get_spaces():
			print "%(key)s: %(name)s" % {
				'key': space.key,
				'name': space.name,
				'url': space.url
			}
	if args[0] == 'get_space':
		try:
			space_key = args[1]
		except IndexError:
			space_key = None
		
		if not space_key:
			space_key = raw_input("> ")
		
		try:
			print c.get_space(space_key)
		except ConfluenceException:
			log.warn(SPACE_NOT_FOUND_OR_AUTH % {'key': space_key})
	
	return c.logout()