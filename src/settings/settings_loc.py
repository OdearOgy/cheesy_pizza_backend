import os 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# don't use this in production
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

# CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

