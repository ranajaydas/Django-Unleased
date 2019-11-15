from django.conf import settings
from django.db import models
from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    joined = models.DateTimeField("Date Joined", auto_now_add=True)

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('public_profile', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('profile_update')


