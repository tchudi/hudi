#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from common.model import Model
from page.bugsearch_page import Bugsearch_page
import unittest
import time

class Search(Model):
    def test_search(self):
        b=Bugsearch_page(self.driver)
        b.search()
        time.sleep(2)
        result=b.sucess_result()
        self.assertTrue(result)


if __name__=="__main__":
    unittest.main()