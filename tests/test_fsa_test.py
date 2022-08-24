#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fsa_test
----------------------------------

Tests for `fsa_test` module.
"""

import unittest

import fsa_test


class TestFsa_test(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, Fahim here!"

    def test_something(self):
	output = fsa_test.hello()
        assert(output == self.hello_message)

    def tearDown(self):
        pass
