# coding: utf-8

"""
    Operation Manager API

    Execute operations with the Operation Manager API.

    OpenAPI spec version: 0.1.4
    
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


class ExecutionPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, operation_instance=None, callback_url=None, force_spawn_cluster=None, resource_provisioner_token=None):
        """
        ExecutionPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operation_instance': 'int',
            'callback_url': 'str',
            'force_spawn_cluster': 'str',
            'resource_provisioner_token': 'str'
        }

        self.attribute_map = {
            'operation_instance': 'operation_instance',
            'callback_url': 'callback_url',
            'force_spawn_cluster': 'force_spawn_cluster',
            'resource_provisioner_token': 'resource_provisioner_token'
        }

        self._operation_instance = operation_instance
        self._callback_url = callback_url
        self._force_spawn_cluster = force_spawn_cluster
        self._resource_provisioner_token = resource_provisioner_token

    @property
    def operation_instance(self):
        """
        Gets the operation_instance of this ExecutionPost.
        Unique ID of the process instance this execution is of

        :return: The operation_instance of this ExecutionPost.
        :rtype: int
        """
        return self._operation_instance

    @operation_instance.setter
    def operation_instance(self, operation_instance):
        """
        Sets the operation_instance of this ExecutionPost.
        Unique ID of the process instance this execution is of

        :param operation_instance: The operation_instance of this ExecutionPost.
        :type: int
        """

        self._operation_instance = operation_instance

    @property
    def callback_url(self):
        """
        Gets the callback_url of this ExecutionPost.
        URL called after completion of the job (possibly empty)

        :return: The callback_url of this ExecutionPost.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this ExecutionPost.
        URL called after completion of the job (possibly empty)

        :param callback_url: The callback_url of this ExecutionPost.
        :type: str
        """

        self._callback_url = callback_url

    @property
    def force_spawn_cluster(self):
        """
        Gets the force_spawn_cluster of this ExecutionPost.
        If set and not empty, forces the creation of a new cluster

        :return: The force_spawn_cluster of this ExecutionPost.
        :rtype: str
        """
        return self._force_spawn_cluster

    @force_spawn_cluster.setter
    def force_spawn_cluster(self, force_spawn_cluster):
        """
        Sets the force_spawn_cluster of this ExecutionPost.
        If set and not empty, forces the creation of a new cluster

        :param force_spawn_cluster: The force_spawn_cluster of this ExecutionPost.
        :type: str
        """

        self._force_spawn_cluster = force_spawn_cluster

    @property
    def resource_provisioner_token(self):
        """
        Gets the resource_provisioner_token of this ExecutionPost.
        Authentication token to be used to connect to the Resource Provisioner

        :return: The resource_provisioner_token of this ExecutionPost.
        :rtype: str
        """
        return self._resource_provisioner_token

    @resource_provisioner_token.setter
    def resource_provisioner_token(self, resource_provisioner_token):
        """
        Sets the resource_provisioner_token of this ExecutionPost.
        Authentication token to be used to connect to the Resource Provisioner

        :param resource_provisioner_token: The resource_provisioner_token of this ExecutionPost.
        :type: str
        """

        self._resource_provisioner_token = resource_provisioner_token

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
