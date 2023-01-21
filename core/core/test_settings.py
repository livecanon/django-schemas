from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "rickandmorty",
        "USER": "rick",
        "PASSWORD": "rick",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "rickandmorty",
            "USER": os.environ.get("TEST_PG_USER"),
            "PASSWORD": os.environ.get("TEST_PG_PASSWORD"),
            "HOST": "127.0.0.1",
            "PORT": 5432,
        }
    }
