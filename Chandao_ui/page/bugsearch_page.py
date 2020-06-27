#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


from common.panduan import Panduan

class Bugsearch_page(Panduan):
    search_loc=('id','searchInput')
    submit_loc=('id','searchGo')

    id_loc=('class name','label-id')


    def search(self,value='031'):
        self.input(self.search_loc,value)
        self.click(self.submit_loc)


    def sucess_result(self):
        return self.text_in_element(self.id_loc,'31')


