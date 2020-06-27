import unittest,logging
from common.desired_caps import appium_desired

from time import sleep
class Myunit(unittest.TestCase):
    def setUp(self):
        logging.info('--setUp--')
        self.dr=appium_desired()



    def tearDown(self):
        logging.info('--tearDown')
        sleep(5)
        self.dr.close_app()
