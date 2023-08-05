# coding=utf8
""" Brain

Handles authorization / user requests
"""

__author__		= "Chris Nasr"
__version__		= "1.0.0"
__copyright__	= "Ouroboros Coding Inc."
__email__		= "chris@ouroboroscoding.com"
__created__		= "2022-08-25"

# Ouroboros imports
from config import config
from upgrade import upgrade

# Python imports
import os
import pathlib
from sys import argv, exit, stderr

# Pip imports
from RestOC import EMail, Record_MySQL, REST, Services, Session

# Module imports
from brain import install, rest

def cli():
	"""CLI

	Called from the command line to run from the current directory

	Returns:
		uint
	"""

	# Get Brain config
	dConfig = config.brain({
		'user_default_locale': 'en-US',
		'mysql_host': 'brain',
		'redis_host': 'brain'
	})

	# Get the data path
	dConfig['data'] = config.services.data('./.data')
	if '~' in dConfig['data']:
		dConfig['data'] = os.path.expanduser(dConfig['data'])
	dConfig['data'] = os.path.abspath(dConfig['data'])

	# Get the module path
	dConfig['module'] = pathlib.Path(__file__).parent.resolve()

	# Add the global prepend
	Record_MySQL.db_prepend(config.mysql.prepend(''))

	# Add the primary mysql DB
	Record_MySQL.add_host('brain', config.mysql.hosts[dConfig['mysql_host']]({
		'host': 'localhost',
		'port': 3306,
		'charset': 'utf8',
		'user': 'root',
		'passwd': ''
	}))

	# Set the timestamp timezone
	Record_MySQL.timestamp_timezone(
		config.mysql.timestamp_timezone('+00:00')
	)

	# If we have no arguments
	if len(argv) == 1:

		# Run the REST server
		return rest.run()

	# Else, if we have one argument
	elif len(argv) == 2:

		# If we are installing
		if argv[1] == 'install':
			return install.install(dConfig)

		# Else, if we are explicitly stating the rest service
		elif argv[1] == 'rest':
			return rest.run()

		# Else, if we are upgrading
		elif argv[1] == 'upgrade':
			return upgrade(dConfig['data'], dConfig['module'])

	# Else, arguments are wrong, print and return an error
	print('Invalid arguments', file=stderr)
	return 1

# Only run if called directly
if __name__ == '__main__':
	exit(cli())