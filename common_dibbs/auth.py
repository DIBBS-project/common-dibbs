# coding: utf-8
from __future__ import absolute_import

import base64
import datetime
import json

import jwt

from . import names


def swagger_basic_auth(swagger_client, username, password):
    authentication_string = '{}:{}'.format(username, password)
    base64_authentication_string = base64.b64encode(authentication_string.encode('utf-8'))
    header_key = "Authorization"
    header_value = "Basic {}".format(base64_authentication_string)
    swagger_client.api_client.default_headers[header_key] = header_value


def seconds_from_now(seconds):
    return datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds)


def obo_token(secret_key, obo_user):
    return jwt.encode(
        payload={
            # standard claim fields
            'iat': seconds_from_now(0),
            'exp': seconds_from_now(30),
            # custom fields
            'dibbs-user': obo_user,
        },
        key=secret_key,
        algorithm='HS256',
    )


def obo_headers(secret_key, obo_user):
    """
    This generates an signed token
    """
    token = obo_token(secret_key, obo_user)

    return {
        names.INTERSERVICE_HEADER: token,
    }
