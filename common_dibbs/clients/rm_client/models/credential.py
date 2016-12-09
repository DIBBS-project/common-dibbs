# coding: utf-8

"""
    Resource manager API

    Manage Cloud Computing resources via API.

    OpenAPI spec version: 0.1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Credential(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, site_name=None, name=None, user=None, credentials=None):
        """
        Credential - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'site_name': 'str',
            'name': 'str',
            'user': 'int',
            'credentials': 'str'
        }

        self.attribute_map = {
            'site_name': 'site_name',
            'name': 'name',
            'user': 'user',
            'credentials': 'credentials'
        }

        self._site_name = site_name
        self._name = name
        self._user = user
        self._credentials = credentials


    @property
    def site_name(self):
        """
        Gets the site_name of this Credential.
        Name of the site

        :return: The site_name of this Credential.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """
        Sets the site_name of this Credential.
        Name of the site

        :param site_name: The site_name of this Credential.
        :type: str
        """
        if site_name is None:
            raise ValueError("Invalid value for `site_name`, must not be `None`")

        self._site_name = site_name

    @property
    def name(self):
        """
        Gets the name of this Credential.
        Name of the credential

        :return: The name of this Credential.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Credential.
        Name of the credential

        :param name: The name of this Credential.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def user(self):
        """
        Gets the user of this Credential.
        ID of the user

        :return: The user of this Credential.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Credential.
        ID of the user

        :param user: The user of this Credential.
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def credentials(self):
        """
        Gets the credentials of this Credential.
        Encrypted credentials (JSON format encrypted)

        :return: The credentials of this Credential.
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this Credential.
        Encrypted credentials (JSON format encrypted)

        :param credentials: The credentials of this Credential.
        :type: str
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
