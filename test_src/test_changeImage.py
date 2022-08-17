#!/usr/bin/env python3

import unittest
import changeImage

class TestChangePath(unittest.TestCase):

    def test_change_ext(self):
        #Valid input
        self.assertEqual(
        change_ext('/abc/xyz/123.txt', 'jpg'), '/abc/xyz/123.jpg')
        # Empty string replacement
        self.assertEqual(
        change_ext('/abc/xyz/123.txt', ''), '/abc/xyz/123')
        #Invalid inputs
        # No Ext
        self.assertRaises(ValueError
        change_ext('/abc/xyz/123', 'jpg'))
        # No source path
        self.assertRaises(ValueError
        change_ext('', 'jpg'), '/abc/xyz/123')



    def test_convert_image(self):
        self.assertEqual(
        change_ext('/abc/xyz/123.txt', 'jpg'), '/abc/xyz/123.jpg')
