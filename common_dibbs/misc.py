# coding: utf-8
from __future__ import absolute_import, print_function


# __all__ = ['configure_basic_authentication']
__all__ = [
    'header_to_metakey',
]


def header_to_metakey(header):
    return 'HTTP_' + header.upper().replace('-', '_')
