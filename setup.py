import os

from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'confluence',
	version = '0.1',
	url = 'http://github.com/myles/confluence',
	license = 'Apache License',
	description = 'A python library to connect to Confluence wiki.',
	long_description = read('README'),
	
	author = 'Myles Braithwaite',
	author_email = 'me@mylesbraithwaite.com',
	
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	
	install_requires = ['setuptools'],
	
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP',
	]
)