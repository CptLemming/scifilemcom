DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOW_ROBOTS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS'   : {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
