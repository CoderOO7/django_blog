from django.db.models.signals import post_save, pre_save
from account.models import Account
from django.dispatch import receiver
from .models import Profile
import os

@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Account)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=Profile)
def delete_old_profile(sender,instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    file = instance.image
    default_image = 'images/profiles/user-avatar.jpeg'
    if old_file != file and old_file != default_image:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)