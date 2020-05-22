
DEGUB=False

# change to your production server's ip
ALLOWED_HOSTS = [

]

CORS_ORIGIN_WHITELIST = [
]


# Your production database settings, set them on the server.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cheesy_pizza',
        'USER': 'pizza_user',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}


