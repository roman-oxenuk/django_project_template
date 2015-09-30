import os
from .common import *


STATIC_FOLDER = 'static_content'
STATIC_ROOT = os.path.join(BASE_DIR, '..', STATIC_FOLDER, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', STATIC_CONTENT, 'media')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'project',
#     }
# }