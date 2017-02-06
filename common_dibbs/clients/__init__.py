# coding: utf-8
from __future__ import absolute_import

from .ar_client.api_client import ApiException as ArApiException
from .om_client.api_client import ApiException as OmApiException
from .or_client.api_client import ApiException as OrApiException
from .rm_client.api_client import ApiException as RmApiException
from .oma_client.api_client import ApiException as OmaApiException
from .rma_client.api_client import ApiException as RmaApiException

ApiException = (
    ArApiException,
    OmApiException,
    OrApiException,
    RmApiException,
    OmaApiException,
    RmaApiException,
)
