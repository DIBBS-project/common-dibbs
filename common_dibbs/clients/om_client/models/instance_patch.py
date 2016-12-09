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


class InstancePatch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, process_definition_id=None, parameters=None, files=None):
        """
        InstancePatch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'process_definition_id': 'int',
            'parameters': 'str',
            'files': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'process_definition_id': 'process_definition_id',
            'parameters': 'parameters',
            'files': 'files'
        }

        self._name = name
        self._process_definition_id = process_definition_id
        self._parameters = parameters
        self._files = files

    @property
    def name(self):
        """
        Gets the name of this InstancePatch.
        Name of the process instance, possibly empty

        :return: The name of this InstancePatch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstancePatch.
        Name of the process instance, possibly empty

        :param name: The name of this InstancePatch.
        :type: str
        """

        self._name = name

    @property
    def process_definition_id(self):
        """
        Gets the process_definition_id of this InstancePatch.
        Unique ID of the operation on which an instance of the operation must be run

        :return: The process_definition_id of this InstancePatch.
        :rtype: int
        """
        return self._process_definition_id

    @process_definition_id.setter
    def process_definition_id(self, process_definition_id):
        """
        Sets the process_definition_id of this InstancePatch.
        Unique ID of the operation on which an instance of the operation must be run

        :param process_definition_id: The process_definition_id of this InstancePatch.
        :type: int
        """

        self._process_definition_id = process_definition_id

    @property
    def parameters(self):
        """
        Gets the parameters of this InstancePatch.
        JSON-formatted string containing a dictionary mapping a value for each parameter declared in the process definition

        :return: The parameters of this InstancePatch.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this InstancePatch.
        JSON-formatted string containing a dictionary mapping a value for each parameter declared in the process definition

        :param parameters: The parameters of this InstancePatch.
        :type: str
        """

        self._parameters = parameters

    @property
    def files(self):
        """
        Gets the files of this InstancePatch.
        JSON-formatted string containing a dictionary mapping each file declared in the process definition to a URL

        :return: The files of this InstancePatch.
        :rtype: str
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this InstancePatch.
        JSON-formatted string containing a dictionary mapping each file declared in the process definition to a URL

        :param files: The files of this InstancePatch.
        :type: str
        """

        self._files = files

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
