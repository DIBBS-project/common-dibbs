# coding: utf-8
from __future__ import absolute_import, print_function

import base64
import json


__all__ = ['configure_basic_authentication']

TEMP_NAME = b'Dibbs-Thing'
TEMP_NAME_DJMETA = TEMP_NAME.upper().replace('-', '_')


def configure_basic_authentication(swagger_client, username, password):
    authentication_string = "{}:{}".format(username, password)
    base64_authentication_string = base64.b64encode(authentication_string.encode('utf-8'))
    header_key = "Authorization"
    header_value = "Basic {}".format(base64_authentication_string)
    swagger_client.api_client.default_headers[header_key] = header_value


def magic_header(username):
    payload = {'user': username}
    encoded = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8'))
    return {TEMP_NAME: encoded}


def add_magic_header(swagger_client, username):
    swagger_client.api_client.default_headers.update(magic_header(username))
