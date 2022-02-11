from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.conf import settings

def user_directory_path(instance, filename):

    return 'contents/UID-{0}/{1}'.format(instance.userFK.id, filename)

class Contents(models.Model):

    CHOICE = (('Image', 'Img'), ('Video', 'VOD'))


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now=True)
    is_Accepted = models.BooleanField(default=True)
    contentType = models.CharField(max_length=200, choices=CHOICE, null=True, default="")

    upload_file = models.FileField(null=True, upload_to=user_directory_path, blank=True)

    theme_id = models.ForeignKey("Theme", related_name="contents", on_delete=models.CASCADE, db_column="theme_id", null=True, blank=True)

    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)

class Contents_Description(models.Model):

    id = models.AutoField(primary_key=True)
    description = HTMLField()
    contentFK = models.ForeignKey(Contents, on_delete=models.CASCADE, db_column="contentsFK", null=True, blank=True)

class Theme(models.Model):

    # CHOICE = (('문화/관광', '문화/관광'), ('스포츠/레저', '스포츠/레저'), ('공예', '공예'), ('연예', '연예'), ('놀이','놀이'))

    id = models.AutoField(primary_key=True)
    # themeValue = models.CharField(max_length=100, choices=CHOICE, null=True, default="")
    themeValue = models.CharField(max_length=100, null=True, default="")

class Detail_Theme(models.Model):

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, null=False)
    theme_id = models.ForeignKey("Theme", related_name="Detail_Theme", on_delete=models.CASCADE, db_column="theme_id")

class Content_Like(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    contents_id = models.ForeignKey("Contents", related_name="Content_Like", on_delete=models.CASCADE, db_column="contents_id")
    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)

class Content_Comment(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    contents_id = models.ForeignKey("Contents", related_name="Content_Comment", on_delete=models.CASCADE, db_column="contents_id")
    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)

