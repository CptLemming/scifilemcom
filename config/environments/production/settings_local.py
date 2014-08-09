DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'OPTIONS'   : {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME'      : 'databasename',
        'USER'      : 'root',
        'PASSWORD'  : '',
        'HOST'      : '127.0.0.1',
        'PORT'      : '',
    }
}
