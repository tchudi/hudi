#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


import unittest

class My(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start---')

    def test_01(self):
        self.assertEqual(2+3,5)

    def test_02(self):
        self.assertTrue(2)

    @classmethod
    def tearDownClass(cls):
        print('end----')

if __name__=="__main__":
    unittest.main()