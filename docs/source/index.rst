.. Confluence documentation master file, created by
   sphinx-quickstart on Thu Apr 30 10:59:32 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

============
pyConfluence
============

pyConfluence is a Python_ library for Atlassian_ Confluence_ Wiki. 

Quick Start
***********

.. code-block:: python
	
	>>> from pyconfluence import Confluence
	>>> c = Confluence('http://localhost:8080/confluence/', 'username', 'password')
	>>> print c.get_server_info()
	Atlassian Confluence 3.0.2

.. code-block:: console
	
	$ confluence -c http://localhost:8080/confluence/ -u username -p password get_server_info
	Atlassian Confluence 3.0.2

You can save the confluence url, username, and password in the configuration file located
in ''~/.pyconfluence.ini''.

.. code-block:: ini
	
	[pyconfluence]
	url=http://localhost:8080/confluence/
	username=username
	password=password

Contents
********

.. toctree::
	:maxdepth: 2
	
	api

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Python: http://python.org/
.. _Atlassian: http://atlassian.com/
.. _Confluence: http://www.atlassian.com/software/confluence/