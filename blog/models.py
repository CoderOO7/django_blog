from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})