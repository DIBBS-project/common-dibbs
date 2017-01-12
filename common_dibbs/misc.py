# coding: utf-8
from __future__ import absolute_import, print_function

import base64


def configure_basic_authentication(swagger_client, username, password):
    authentication_string = "{}:{}".format(username, password)
    base64_authentication_string = base64.b64encode(authentication_string.encode('utf-8'))
    header_key = "Authorization"
    header_value = "Basic {}".format(base64_authentication_string)
    swagger_client.api_client.default_headers[header_key] = header_value
