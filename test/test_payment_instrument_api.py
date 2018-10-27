# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.payment_instrument_api import PaymentInstrumentApi


class TestPaymentInstrumentApi(unittest.TestCase):
    """ PaymentInstrumentApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.payment_instrument_api.PaymentInstrumentApi()

    def tearDown(self):
        pass

    def test_paymentinstruments_post(self):
        """
        Test case for paymentinstruments_post

        Create a Payment Instrument
        """
        pass

    def test_paymentinstruments_token_id_delete(self):
        """
        Test case for paymentinstruments_token_id_delete

        Delete a Payment Instrument
        """
        pass

    def test_paymentinstruments_token_id_get(self):
        """
        Test case for paymentinstruments_token_id_get

        Retrieve a Payment Instrument
        """
        pass

    def test_paymentinstruments_token_id_patch(self):
        """
        Test case for paymentinstruments_token_id_patch

        Update a Payment Instrument
        """
        pass


if __name__ == '__main__':
    unittest.main()
