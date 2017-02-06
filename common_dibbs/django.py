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
import jwt
import requests
from rest_framework.authentication import BaseAuthentication

from .auth import obo_headers as _auth_obo_headers
from .misc import header_to_metakey
from . import names

__all__ = [
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
            auth_header = request.META.pop(names.AUTHORIZATION_HEADER_METAKEY)
        except KeyError:
            return

        # save token for easier forwarding
        request.dibbs_token = auth_header

        response = requests.get(
            url='{}/auth/tokens'.format(settings.DIBBS['urls']['cas']),
            headers={
                names.AUTHORIZATION_HEADER: auth_header,
            },
        )
        if response.status_code != 200:
            self.logger.info('failed to authenticate user (provided token: \'{}\')'.format(auth_header))
            raise PermissionDenied('authentication failed')

        auth_data = response.json()
        self.logger.debug('provided auth_data: {}'.format(auth_data))

        dibbs_user = auth_data['username']
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
        request.dibbs_interservice = False
        jwt_key = settings.DIBBS['shared_secret']
        try:
            token = request.META[names.INTERSERVICE_HEADER_METAKEY]
        except KeyError:
            return

        try:
            payload = jwt.decode(
                token,
                key=jwt_key,
                algorithms=['HS256'],
                leeway=10, # seconds
                # https://github.com/jpadilla/pyjwt/issues/190
                options={'verify_iat': False},
            )
        except jwt.exceptions.InvalidTokenError as e:
            logger.info('refused token "{}" because "{}"'.format(token[:2000], str(e)))
            raise PermissionDenied(str(e))

        dibbs_user = payload['dibbs-user']
        logger.info('authenticated "{}" via interservice signed token'.format(dibbs_user))
        request.dibbs_interservice = True
        request.META['REMOTE_USER'] = dibbs_user


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


def obo_headers(obo_user):
    """
    Convienence for ``common_dibbs.auth.obo_headers`` that pulls in the
    shared key from Django settings.
    """
    key = settings.DIBBS['shared_secret']
    return _auth_obo_headers(key, obo_user)


def relay_swagger(swagger_client, incoming_request=None):
    headers = obo_headers(incoming_request.user.username)
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
