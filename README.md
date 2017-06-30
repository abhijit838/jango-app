# jango-app
First django app

* $ django-admin startproject mysite .
* $ python manage.py migrate
* $ python manage.py runserver
* $ python manage.py startapp blog
* Add the app to settings.py -> INSTALLED_APPS -> 'blog'
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'blog', <--- here
]

* Create model
from future import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

```python
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def str(self):
		return self.title
```
* Create migration for model $ python manage.py makemigrations blog, 
* Apply migration to create model in database $ python manage.py migrate blog
* To do any operation on model we will use admin
* Register model in admin → admin.site.register(Post)
* Create super user to login to admin $ python manage.py createsuperuser
* Browse /admin and login with username password
* Post your blog content
