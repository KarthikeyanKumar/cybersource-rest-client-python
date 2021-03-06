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


class Tmsv1paymentinstrumentsBuyerInformation(object):
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
        'company_tax_id': 'str',
        'currency': 'str',
        'date_o_birth': 'str',
        'personal_identification': 'list[Tmsv1paymentinstrumentsBuyerInformationPersonalIdentification]'
    }

    attribute_map = {
        'company_tax_id': 'companyTaxID',
        'currency': 'currency',
        'date_o_birth': 'dateOBirth',
        'personal_identification': 'personalIdentification'
    }

    def __init__(self, company_tax_id=None, currency=None, date_o_birth=None, personal_identification=None):
        """
        Tmsv1paymentinstrumentsBuyerInformation - a model defined in Swagger
        """

        self._company_tax_id = None
        self._currency = None
        self._date_o_birth = None
        self._personal_identification = None

        if company_tax_id is not None:
          self.company_tax_id = company_tax_id
        if currency is not None:
          self.currency = currency
        if date_o_birth is not None:
          self.date_o_birth = date_o_birth
        if personal_identification is not None:
          self.personal_identification = personal_identification

    @property
    def company_tax_id(self):
        """
        Gets the company_tax_id of this Tmsv1paymentinstrumentsBuyerInformation.
        Company Tax ID.

        :return: The company_tax_id of this Tmsv1paymentinstrumentsBuyerInformation.
        :rtype: str
        """
        return self._company_tax_id

    @company_tax_id.setter
    def company_tax_id(self, company_tax_id):
        """
        Sets the company_tax_id of this Tmsv1paymentinstrumentsBuyerInformation.
        Company Tax ID.

        :param company_tax_id: The company_tax_id of this Tmsv1paymentinstrumentsBuyerInformation.
        :type: str
        """
        if company_tax_id is not None and len(company_tax_id) > 9:
            raise ValueError("Invalid value for `company_tax_id`, length must be less than or equal to `9`")

        self._company_tax_id = company_tax_id

    @property
    def currency(self):
        """
        Gets the currency of this Tmsv1paymentinstrumentsBuyerInformation.
        Currency. Accepts input in the ISO 4217 standard, stores as ISO 4217 Alpha

        :return: The currency of this Tmsv1paymentinstrumentsBuyerInformation.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Tmsv1paymentinstrumentsBuyerInformation.
        Currency. Accepts input in the ISO 4217 standard, stores as ISO 4217 Alpha

        :param currency: The currency of this Tmsv1paymentinstrumentsBuyerInformation.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")

        self._currency = currency

    @property
    def date_o_birth(self):
        """
        Gets the date_o_birth of this Tmsv1paymentinstrumentsBuyerInformation.
        Date of birth YYYY-MM-DD.

        :return: The date_o_birth of this Tmsv1paymentinstrumentsBuyerInformation.
        :rtype: str
        """
        return self._date_o_birth

    @date_o_birth.setter
    def date_o_birth(self, date_o_birth):
        """
        Sets the date_o_birth of this Tmsv1paymentinstrumentsBuyerInformation.
        Date of birth YYYY-MM-DD.

        :param date_o_birth: The date_o_birth of this Tmsv1paymentinstrumentsBuyerInformation.
        :type: str
        """

        self._date_o_birth = date_o_birth

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this Tmsv1paymentinstrumentsBuyerInformation.

        :return: The personal_identification of this Tmsv1paymentinstrumentsBuyerInformation.
        :rtype: list[Tmsv1paymentinstrumentsBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this Tmsv1paymentinstrumentsBuyerInformation.

        :param personal_identification: The personal_identification of this Tmsv1paymentinstrumentsBuyerInformation.
        :type: list[Tmsv1paymentinstrumentsBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

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
        if not isinstance(other, Tmsv1paymentinstrumentsBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
