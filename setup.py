from setuptools import setup, find_packages

setup(
	name = 'confluence',
	version = '0.1',
	url = 'http://github.com/myles/confluence',
	license = '',
	description = 'A python library to connect to Confluence wiki.',
	author = 'Myles Braithwaite',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = ['setuptools'],
)