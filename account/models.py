from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# create a newuser
# create a supseruser


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name=' ', last_name=' '):
        user = self.create_user(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = None
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(default='', max_length=30)
    last_name = models.CharField(default='', max_length=30)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    # bind that AccountManager to our model
    objects = MyAccountManager()

    # Allow to use email to login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'images/profiles/{self.pk}/'):]

    def get_full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
