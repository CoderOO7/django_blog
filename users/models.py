from django.db import models
from django.conf import settings
from account.models import Account
from PIL import Image
import uuid
import os


def get_profile_image_file_path(self, filename):
    return f'images/profiles/{uuid.uuid4().hex}-{filename}'


def get_default_profile_image():
    return 'images/profiles/user-avatar.jpeg'


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default=get_default_profile_image, upload_to=get_profile_image_file_path)

    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if os.path.isfile(self.image.path):
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
