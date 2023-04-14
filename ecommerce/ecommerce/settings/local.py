import os

from dotenv import load_dotenv

from .base import *

load_dotenv()
# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# SECRET_KEY

SECRET_KEY = os.environ.get("SECRET_KEY")
