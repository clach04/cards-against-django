import urlparse
from .local import *

KEEN_PROJECT_ID = get_env_variable("KEEN_ID")
KEEN_WRITE_KEY = get_env_variable("KEEN_WRITE_KEY")

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

REDIS_URL = urlparse.urlparse(get_env_variable('REDISCLOUD_URL'))
SOCKETIO_URL = 'localhost'