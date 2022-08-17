#!/usr/bin/env python3

import test_constants
import unittest
from changeImage import change_ext
from changeImage import convert_image_to_JPEG

class TestChangePath(unittest.TestCase):

    def test_change_ext(self):
        #Valid input
        self.assertEqual(
        change_ext('/abc/xyz/123.txt', '.jpg'), '/abc/xyz/123.jpg')
        # Empty string replacement
        self.assertEqual(
        change_ext('/abc/xyz/123.txt', ''), '/abc/xyz/123')
        #Invalid inputs
        # No source path
        self.assertRaises(ValueError, change_ext, '', '.jpg')

    def test_convert_image(self):
        self.assertTrue(convert_image_to_JPEG(test_constants.tiff_imgs_test_data_dir + "01.tiff"))

if __name__ == '__main__':
    unittest.main()
