# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_self': 'TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksSelf',
        'first': 'TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksFirst',
        'prev': 'TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksPrev',
        'next': 'TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksNext',
        'last': 'TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksLast'
    }

    attribute_map = {
        '_self': 'self',
        'first': 'first',
        'prev': 'prev',
        'next': 'next',
        'last': 'last'
    }

    def __init__(self, _self=None, first=None, prev=None, next=None, last=None):
        """
        TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks - a model defined in Swagger
        """

        self.__self = None
        self._first = None
        self._prev = None
        self._next = None
        self._last = None

        if _self is not None:
          self._self = _self
        if first is not None:
          self.first = first
        if prev is not None:
          self.prev = prev
        if next is not None:
          self.next = next
        if last is not None:
          self.last = last

    @property
    def _self(self):
        """
        Gets the _self of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :return: The _self of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :param _self: The _self of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :type: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksSelf
        """

        self.__self = _self

    @property
    def first(self):
        """
        Gets the first of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :return: The first of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksFirst
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :param first: The first of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :type: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksFirst
        """

        self._first = first

    @property
    def prev(self):
        """
        Gets the prev of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :return: The prev of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksPrev
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """
        Sets the prev of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :param prev: The prev of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :type: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksPrev
        """

        self._prev = prev

    @property
    def next(self):
        """
        Gets the next of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :return: The next of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksNext
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :param next: The next of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :type: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksNext
        """

        self._next = next

    @property
    def last(self):
        """
        Gets the last of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :return: The last of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksLast
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.

        :param last: The last of this TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks.
        :type: TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinksLast
        """

        self._last = last

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
        if not isinstance(other, TmsV1InstrumentidentifiersPaymentinstrumentsGet200ResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other