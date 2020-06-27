from businessView.forum import ForumView
import unittest
from time import sleep
from common.desired_caps import appium_desired

class Forumtest(unittest.TestCase):
    def setUp(self):
        self.dr=appium_desired()
        self.f=ForumView(self.dr)
        self.f.check_is_login()

    def tearDown(self):
        sleep(5)
        self.dr.close_app()

    def test_forum(self):
        self.f.forum_send()
        result=self.f.forum_send_status()
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()


