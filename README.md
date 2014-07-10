Django Boilerplate for Django 1.6 with Django CMS 3.0
=================================

### Usage
This assumes you have pip and django installed (if not, try `$ sudo easy_install pip`)

	$ django-admin.py startproject --template http://github.com/jp74/cms-boilerplate/zipball/master project_name
	$ cd project_name
	$ pip install -r requirements.txt
	$ python manage.py syncdb --migrate
	$ cd config; ln -s environments/production/settings_local.py settings_local.py

### Settings
Django settings are configured in `config/settings_common.py` and any settings added in `config/settings_local.py` will be picked up and override any previously defined settings.

### Preinstalled Apps
 * [path.py](https://github.com/dottedmag/path.py): A module wrapper for os.path
 * [South](http://south.aeracode.org/): Intelligent database migrations
 * [django-compressor](https://github.com/jezdez/django_compressor): Compresses linked and inline javascript or CSS into a single cached file.

### Credits
https://github.com/nathanwalsh/django-boilerplate/
https://github.com/martinogden/django-boilerplate/
http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/
