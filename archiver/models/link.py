from datetime import datetime
from uuid import uuid4

from archiver.models.link_token import LinkToken

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError
from django.db import models


class Link(models.Model):
    link = models.URLField('Link')
    identifier = models.UUIDField(
        'Identifier',
        unique=True,
        default=uuid4,
        editable=False
    )
    internet_archive = models.URLField(
        'Archived version of page',
        blank=True,
        default=None
    )
    internet_archive_datetime = models.DateTimeField(
        'Time of archived version creation',
        null=True,
        blank=True,
        default=None
    )
    expiration = models.DateTimeField(
        'Link expiration',
        null=True,
        blank=True,
        default=None
    )
    creation = models.DateTimeField(
        'Date and time og link archival',
        default=datetime.now,
        editable=False
    )
    restricted = models.BooleanField('Access is restricted to people with a token')
    creator = models.ForeignKey(
        get_user_model(),
        blank=False
    )

    def clean(self, *args, **kwargs):
        if (self.internet_archive is '') != (self.internet_archive_datetime is None):
            # Fail if either is set and the other is not
            raise ValidationError('Both internet_archive and internet_archive_datetime has to be set or not')
        super(Link, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Link, self).save(*args, **kwargs)

    def delete_access_tokens(self):
        LinkToken.objects.filter(link=self).delete()
