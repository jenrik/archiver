from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


class LinkToken(models.Model):
    link = models.ForeignKey('Link', on_delete=models.CASCADE)
    token = models.UUIDField('Access token', default=uuid4)
    expiration = models.DateTimeField('Date and time of invalidation', null=True, blank=True)
    creator = models.ForeignKey(get_user_model())
