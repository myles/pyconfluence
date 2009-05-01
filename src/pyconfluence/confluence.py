import sys

from pyconfluence import __version__

def usage(argv, msg=None):
	if msg:
		print >>sys.stderr, msg
		print >>sys.stderr
	print >>sys.stderr, """\
pyConfluence v%(version)s
Usage: %(argv)s
Options:
""" % { 'version': __version__, 'argv': argv }

def main(argv=sys.argv):
	return usage(argv)