# coding=utf8
""" Access

Shared methods for verifying access
"""

__author__ = "Chris Nasr"
__copyright__ = "Ouroboros Coding Inc"
__version__ = "1.0.0"
__email__ = "chris@ouroboroscoding.com"
__created__ = "2022-08-29"

# Pip imports
from RestOC import Errors, REST, Services

# Package imports
from body import errors

READ = REST.READ
R = REST.READ
"""Allowed to read records"""

UPDATE = REST.UPDATE
U = REST.UPDATE
"""Allowed to update records"""

CREATE = REST.CREATE
C = REST.CREATE
"""Allowed to create records"""

DELETE = REST.DELETE
D = REST.DELETE
"""Allowed to delete records"""

ALL = REST.ALL
A = REST.ALL
"""Allowed to CRUD"""

CREATE_UPDATE_DELETE = REST.CREATE_UPDATE_DELETE
CUD = REST.CREATE_UPDATE_DELETE
"""Create, Delete, and Update"""

CREATE_READ_DELETE = REST.CREATE_READ_DELETE
CRD = REST.CREATE_READ_DELETE
"""Create, Read, and Delete"""

READ_UPDATE = REST.READ_UPDATE
RU = REST.READ_UPDATE
"""Read and Update"""

def verify(sesh, name, right):
	"""Verify

	Checks's if the currently signed in user has the requested right on the
	given permission. If the user has rights, nothing happens, else an
	exception of ResponseException is raised

	Arguments:
		sesh (RestOC.Session._Session): The current session
		name (str|str[]): The name(s) of the permission to check
		right (uint|uint[]): The right(s) to check for

	Raises:
		ResponseException

	Returns:
		bool
	"""

	# Init request data
	dData = {
		'name': name,
		'right': right
	}

	# Check with the authorization service
	oResponse = Services.read('brain', 'verify', {
		'data': dData,
		'session': sesh
	})

	# If the response failed
	if oResponse.error_exists():
		raise Services.ResponseException(oResponse)

	# If the check failed, raise an exception
	if not oResponse.data:
		raise Services.ResponseException(error=errors.RIGHTS)

	# Return OK
	return True

def verify_return(sesh, name, right, ident=None):
	"""Verify Return

	Same as verify, but returns the result instead of raising an exception

	Arguments:
		sesh (RestOC.Session._Session): The current session
		name (str): The name of the permission to check
		right (uint): The right to check for
		ident (str): Optional identifier to check against

	Returns:
		bool
	"""

	try:
		verify(sesh, name, right, ident)
		return True
	except Services.ResponseException as e:
		if e.error['code'] == errors.RIGHTS:
			return False
		else:
			raise e

def internal(data):
	""" Internal

	Checks for an internal key and throws an exception if it's missing or
	invalid

	Arguments:
		data (dict): Data to check for internal key

	Raises:
		ResponseException

	Returns:
		None
	"""

	# If the key is missing
	if '_internal_' not in data:
		raise Services.ResponseException(error=(errors.BODY_FIELD, [('_internal_', 'missing')]))

	# Verify the key, remove it if it's ok
	if not Services.internal_key(data['_internal_']):
		raise Services.ResponseException(error=Errors.SERVICE_INTERNAL_KEY)
	del data['_internal_']

def internal_or_verify(req, name, right):
	""" Internal or Verify

	Checks for an internal key, if it wasn't sent, does a verify check

	Arguments:
		req (dict): The request details, which can include 'data' and 'session'
		name (str): The name of the permission to check
		right (uint): The right to check for

	Raises:
		ResponseException

	Returns:
		None
	"""

	# If this is an internal request
	if '_internal_' in req['data']:

		# Verify the key, remove it if it's ok
		if not Services.internal_key(req['data']['_internal_']):
			raise Services.ResponseException(error=Errors.SERVICE_INTERNAL_KEY)
		del req['data']['_internal_']

	# Else,
	else:

		# If there's no session
		if 'session' not in req or not req['session']:
			return Services.Error(Errors.REST_AUTHORIZATION, 'Unauthorized')

		# Make sure the user has the proper permission to do this
		verify(req['session'], name, right)