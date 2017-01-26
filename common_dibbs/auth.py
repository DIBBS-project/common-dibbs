# coding: utf-8
from __future__ import absolute_import

import base64
import json

from . import names


def swagger_basic_auth(swagger_client, username, password):
    authentication_string = '{}:{}'.format(username, password)
    base64_authentication_string = base64.b64encode(authentication_string.encode('utf-8'))
    header_key = "Authorization"
    header_value = "Basic {}".format(base64_authentication_string)
    swagger_client.api_client.default_headers[header_key] = header_value


def enc_token(token):
    return b'Bearer {}'.format(
        base64.urlsafe_b64encode(
            json.dumps(token)
            .encode('utf-8'))
        .decode('ascii')
    )


def client_auth_headers(username, password=None):
    """
    This generates an UNSIGNED token, i.e. FIX ME (and the thing that consumes
    it)
    """
    token = enc_token({'dibbs_user': username, 'password': password})

    return {
        names.AUTHORIZATION_HEADER: token,
    }
