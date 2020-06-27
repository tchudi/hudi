from baseView.baseView import BaseView
#from common.desired_caps import appium_desired
import logging
from selenium.webdriver.common.by import By
import time,os



class Common(BaseView):



    def check_cancelBtn(self):
        logging.info('====check_cancelBtn====')
        try:
            element=self.dr.find_element(self.cancelBtn)
        except:
            logging.info('no cancelBtn')
        else:
            element.click()

    def check_skipBtn(self):
        logging.info('====check_skipBtn====')
        try:
            element=self.dr.find_element(self.skipBtn)
        except:
            logging.info('no skipBtn')
        else:
            element.click()


    def get_size(self):
        x=self.get_window_size()['width']
        y=self.get_window_size()['height']
        return x,y


    def swipeleft(self):
        logging.info('swipeleft')
        l=self.get_size()
        x1=int(l[0]*0.9)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)


    def get_time(self):
        now=time.strftime('%Y-%m-%d_%H-%M-%S')
        return now

    def getscreenshot(self,model):
        now=self.get_time()
        file='../screenshot/%s_%s.png'%(model,now)
        self.dr.get_screenshot_as_file(file)


    def check_market_ad(self):
        logging.info('====check_market_ad====')
        try:
            element=self.dr.find_element(self.check_market_ad)

        except:
            logging.info('no market_ad')

        else:
            logging.info("====close market ad")
            element.click()


if __name__=="__main__":
    dr=appium_desired()
    com=Common(dr)
    com.check_cancelBtn()
    com.check_skipBtn()
    com.check_market_ad()

    #com.swipeleft()
    com.getscreenshot('start app')
    time.sleep(5)
    com.close()

