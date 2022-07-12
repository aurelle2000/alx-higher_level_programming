#!/usr/bin/python3
""" test Task 17 """

import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_from_json_string(self):
        string_js = '[{"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}, \
            {"id": 7, "width": 1, "height": 7, "x": 6, "y": 5}]'
        jsonconv = Base.from_json_string(string_js)
        self.assertTrue(type(jsonconv) is list)
        self.assertEqual(len(jsonconv), 2)
