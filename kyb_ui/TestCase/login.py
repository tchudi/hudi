
from businessView.loginView import LoginView
import unittest
#from common.desired_caps import appium_desired
from config.capability import capability
from time import sleep
class Login(unittest.TestCase):
    def setUp(self):
        self.dr=capability()
    def tearDown(self):
        sleep(5)
        self.dr.close_app()


    def test_login(self):
        l=LoginView(self.dr)
        l.login_action('ILOVET','admin888')
        result=l.check_login_status()
        self.assertTrue(result)

    def test_login_error(self):
        l = LoginView(self.dr)
        l.login_action('ILOVETtt', 'admin888')
        result = l.check_login_status()
        self.assertFalse(result)

if __name__=='__main__':
    unittest.main()
