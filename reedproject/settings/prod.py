from .base import *
from decouple import config
import dj_database_url

DEBUG = FALSE

ALLOWED_HOSTS = [".herokuapp.com"]

DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net",
    "https://*.herokuapp.com",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"