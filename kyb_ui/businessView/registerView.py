#from common.common_fun import Common
from common.desired_caps import appium_desired
from businessView.loginView import LoginView
from selenium.webdriver.common.by import By
import logging,time,random


class RegisterView(LoginView):
    myself_loc = (By.ID, "com.tal.kaoyan:id/mainactivity_button_mysefl")
    login_loc = (By.ID, "com.tal.kaoyan:id/activity_usercenter_userheader")

    register_loc=(By.ID,"com.tal.kaoyan:id/login_register_text")

    # now=time.strftime("%Y%m%d%H%M%S")
    # username='admin'+now

    username=(By.ID,"com.tal.kaoyan:id/activity_register_username_edittext")
    password=(By.ID,"com.tal.kaoyan:id/activity_register_password_edittext")
    email=(By.ID,"com.tal.kaoyan:id/activity_register_email_edittext")
    registerBtn=(By.ID,"com.tal.kaoyan:id/activity_register_register_btn")

    userheader=(By.ID,"com.tal.kaoyan:id/activity_usercenter_userheader")
    city=(By.ID,"com.tal.kaoyan:id/activity_myinfo_city_relativelayout")
    school=(By.ID,"com.tal.kaoyan:id/activity_myinfo_bschool_relativelayout")
    year=(By.ID,'com.tal.kaoyan:id/activity_myinfo_year_relativelayout')
    zhuanye=(By.ID,"com.tal.kaoyan:id/activity_myinfo_majorinfo_relativelayout")
    yschool=(By.ID,"com.tal.kaoyan:id/activity_myinfo_schtextview")
    leftbutton=(By.ID,"com.tal.kaoyan:id/myapptitle_leftbutton_image")

    username_loc=(By.ID,"com.tal.kaoyan:id/activity_usercenter_username")


    def register_action(self,username,password,email):
        logging.info('====register_action====')
        self.dr.find_element(*self.myself_loc).click()
        self.dr.find_element(*self.login_loc).click()
        self.dr.find_element(*self.register_loc).click()
        self.dr.find_element(*self.username).send_keys(username)
        self.dr.find_element(*self.password).send_keys(password)
        self.dr.find_element(*self.email).send_keys(email)
        self.dr.find_element(*self.registerBtn).click()


    def check_register(self):
        logging.info('====check register====')
        try:
            self.dr.find_element(*self.username_loc)
        except:
            logging.error("register fail")
            return False
        else:
            logging.info('register sucess')
            self.logout()
            return True

if __name__=="__main__":
    dr=appium_desired()
    r=RegisterView(dr)
    username='gutianle'+str(random.randint(100,1000))
    password='admin888'
    email=str(random.randint(100000000,10000000000))+'@qq.com'
    r.register_action(username,password,email)
    r.check_register()











