from .base import *
from decouple import config
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = [".herokuapp.com"]

DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL"))
}

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net",
    "https://*.herokuapp.com",
]