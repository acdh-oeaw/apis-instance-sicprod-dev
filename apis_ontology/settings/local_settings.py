# Template for file for local Django settings.
#
# To be used as basis for new settings files for local development,
# to store keys/passwords, values for development databases etc.
#
# Resulting local settings files are not meant to be committed/versioned.

from .server_settings import *

print("using apis ontology local settings")

# DEBUG, DEV_VERSION are optional variables which override defaults
# for production environments set in server_settings.py
# Comment them out if/when they are not needed.
DEBUG = True
DEV_VERSION = False

# Database settings for MySQL / MariaDB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "apis_sicprod",
        "USER": "apis_sicprod_user",
        "PASSWORD": "apissicprodpassword",
        #"HOST": "192.168.110.127",  # use "localhost" or the IP address your DB is hosted on
        "HOST": "127.0.0.1",  # use "localhost" or the IP address your DB is hosted on
        "PORT": "3306",
    }
}

INSTALLED_APPS.append('django_extensions')

#ONTOLOGY_DIR = os.path.dirname(
#    os.path.dirname(__file__)
#)
#print(ONTOLOGY_DIR)
#for template in TEMPLATES:
#  template["DIRS"].append(os.path.join(ONTOLOGY_DIR, "templates"))
print(ROOT_URLCONF)
