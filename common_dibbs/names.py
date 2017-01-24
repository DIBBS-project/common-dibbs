# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from .misc import header_to_metakey


AUTHORIZATION_HEADER = 'Dibbs-Authorization'
AUTHORIZATION_HEADER_KEY = header_to_metakey(AUTHORIZATION_HEADER)
INTERSERVICE_HEADER = 'Dibbs-Interservice'
INTERSERVICE_HEADER_KEY = header_to_metakey(INTERSERVICE_HEADER)
