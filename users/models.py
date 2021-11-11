from django.db import models
from account.models import Account
import uuid


def get_profile_image_file_path(self, filename):
    return f'images/profiles/{uuid.uuid4().hex}-{filename}'


def get_default_profile_image():
    return 'images/profiles/user-avatar.jpeg'


class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    image = models.ImageField(default=get_default_profile_image, upload_to=get_profile_image_file_path)

    def __str__(self):
        return f'{self.user.email} Profile'

