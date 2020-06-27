from common.myunit import Myunit
import unittest
from businessView.registerView import RegisterView
import random
class Retister(Myunit):


    def test_register(self):
        r=RegisterView(self.dr)
        username='zhangxueyou'+str(random.randint(100,1000))
        password='admin888'
        email=str(random.randint(100000,10000000))+'@qq.com'
        r.register_action(username,password,email)
        r.check_register()

if __name__=="__main__":
    unittest.main()