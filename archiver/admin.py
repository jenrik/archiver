from archiver.models.link import Link
from archiver.models.link_token import LinkToken

from django.contrib import admin


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('identifier', 'creation')


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkToken)
