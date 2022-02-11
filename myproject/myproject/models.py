from cms.models.pluginmodel import CMSPlugin
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import views as auth_views
class Poem(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')
    # body = models.CharField(max_length=1000, default='MyPoem')
    body = HTMLField()

class TestModel(models.Model):
    name = models.CharField(max_length=100)

####################################################
