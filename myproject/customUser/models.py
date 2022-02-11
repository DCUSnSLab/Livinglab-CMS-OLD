from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Profile/UID-{0}/{1}'.format(instance.user.id, filename)

SYSTEM_AUTHORITY = (
        ('SUPER_ADMIN', 'Super_Admin'),
        ('SHELTER_ADMIN', 'Shelter_Admin'),
        ('CONTENTS_CREATOR', 'Contents_CREATOR'),
        ('USER', 'User'),
    )

class CustomUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=0)
    user_description = models.TextField(max_length=500, blank=True, null=True, default=0)
    user_profile = models.ImageField(null=True, upload_to=user_directory_path, blank=True)
    user_auth = models.CharField(max_length=200, choices=SYSTEM_AUTHORITY, null=True, default=0)

    def __str__(self):
        return self.user.username


