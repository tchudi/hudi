#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        print('start---')

    def tearDown(self):
        print('end_---')

    def test_01(self):
        self.assertEqual(1+2,3)

    def test_02(self):
        self.assertEqual(2-3,-1)


if __name__=="__main__":
    unittest.main()