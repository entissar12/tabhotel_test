from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .constants import STATUS_CHOICES, CATEGORY_CHOICES
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def images_folder(instance, filename):
    return 'media/tickets/images/{}'.format(filename)


class Ticket(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to=images_folder,
        null=True,
        blank=True
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
