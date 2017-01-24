# coding: utf-8
"""
Django-specific components. Importing this without Django configured will
throw warnings.
"""
from __future__ import absolute_import, print_function, unicode_literals

import base64
import json
import logging

from django.conf import settings
from django.contrib.auth import backends as django_backends
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
import requests
from rest_framework.authentication import BaseAuthentication

from .misc import header_to_metakey
from . import names

__all__ = [
    'AUTHORIZATION_HEADER',
    'INTERSERVICE_HEADER',
    'CASUserBridgeMiddleware',
    'InterserviceMiddleware',
    'relay_headers',
    'relay_swagger',
]

logger = logging.getLogger(__name__)


class CASUserBridgeMiddleware(object):
    """
    This middleware is designed to transform the Authorization HTTP header
    into a REMOTE_USER for consumption by the Django RemoteUserMiddleware
    which will generate a database entry for that user.

    .. note::

        By passing this middleware, the user is thus authenticated: having
        ``request.META['REMOTE_USER']`` set signals to the ``RemoteUser``
        backend that authentication has succeeded.
    """
    def __init__(self, *args, **kwargs):
        super(CASUserBridgeMiddleware, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger('{}.{}'.format(__name__, self.__class__.__name__))

    def process_request(self, request):
        try:
            auth_header = request.META.pop(names.AUTHORIZATION_HEADER_KEY)
        except KeyError:
            return

        # save token for easier forwarding
        request.dibbs_token = auth_header

        bearer_prefix = b'Bearer '
        if not auth_header.startswith(bearer_prefix):
            return HttpResponseBadRequest('Token (Bearer) auth only.')
        auth_header = auth_header[len(bearer_prefix):]
        auth_data = json.loads(base64.urlsafe_b64decode(auth_header).decode('utf-8'))

        self.logger.debug('provided auth_data: {}'.format(json.dumps(auth_data)))

        # TODO: verify the auth payload against the CAS and get the username
        dibbs_user = auth_data['dibbs_user']
        # HACK: pretend users
        self.logger.info('user = \'{}\''.format(dibbs_user))

        if dibbs_user not in ['alice', 'bob', 'cindy', 'dave']:
            self.logger.info('failed to authenticate user (provided: \'{}\')'.format(dibbs_user))
            raise PermissionDenied('non-existant user. go away.')

        self.logger.info('authenticated user/REMOTE_USER set as: \'{}\''.format(dibbs_user))
        request.META['REMOTE_USER'] = dibbs_user


class InterserviceMiddleware(object):
    """
    This middleware is designed to detect valid inter-service requests on
    behalf of a user and hang additional
    """
    def __init__(self, *args, **kwargs):
        # super(InterserviceMiddleware, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger('{}.{}'.format(__name__, self.__class__.__name__))

    def process_request(self, request):
        # TODO: secure this (shared secret or whatever)
        if request.META.get(names.INTERSERVICE_HEADER_KEY, False):
            request.dibbs_interservice = True
        else:
            request.dibbs_interservice = False


class DRFAuthentication(BaseAuthentication):
    """
    Mostly copied from rest_framework.authentication.SessionAuthentication
    because we're using Django middleware machinery to do the authentication
    anyways which sets ``request.user`` (for Django's request, not DRF's
    wrapped request). This just ignores the CSRF stuff (shouldn't be
    applicable if using tokens?)
    """
    def authenticate(self, request):
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """
        # Get the session-based user from the underlying HttpRequest object
        user = getattr(request._request, 'user', None)

        # Unauthenticated
        if not user or not user.is_active:
            return None

        return (user, None)


def relay_headers(incoming_request):
    return {
        names.AUTHORIZATION_HEADER: incoming_request.dibbs_token,
        names.INTERSERVICE_HEADER: True,
    }


def relay_swagger(swagger_client, incoming_request=None):
    headers = relay_headers(incoming_request)
    swagger_client.api_client.default_headers.update(headers)


##############
# HACK: http://stackoverflow.com/q/18605259/194586

from threading import local

_active = local()

def get_request():
    return _active.request

class GlobalRequestMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        _active.request = request
        return None

##############
