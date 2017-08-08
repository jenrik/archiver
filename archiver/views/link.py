import uuid

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from archiver.models.link import Link


def redirect_link_original(request, identifier):
    try:
        identifier = uuid.UUID(identifier)
    except ValueError:
        return HttpResponseBadRequest("Invalid identifier")
    link = get_object_or_404(Link, identifier=identifier)
    # ToDo: Check expiration
    return redirect(link.link)


def redirect_link_archive(request, identifier):
    try:
        identifier = uuid.UUID(identifier)
    except ValueError:
        return HttpResponseBadRequest("Invalid identifier")
    link = get_object_or_404(Link, identifier=identifier)
    # ToDo: check expiration
    if link.internet_archive is '':
        # Page have not been archived yet
        return HttpResponse('Link has not yet been archived', status=204)
    else:
        return redirect(link.internet_archive)

# ToDo: create a view exposing metadata for a link
# Optinal format? human (html), json, xml
