from common.common_fun import Common
from selenium.webdriver.common.by import By
import logging
import logging.config
from common.desired_caps import appium_desired
class LoginView(Common):
    myself_loc=(By.ID,"com.tal.kaoyan:id/mainactivity_button_mysefl")
    login_loc=(By.ID,"com.tal.kaoyan:id/activity_usercenter_userheader")

    username_loc=(By.ID,"com.tal.kaoyan:id/login_email_edittext")
    password_loc=(By.ID,"com.tal.kaoyan:id/login_password_edittext")
    loginBtn=(By.ID,"com.tal.kaoyan:id/login_login_btn")

    username_info=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    setting_loc=(By.ID,"com.tal.kaoyan:id/myapptitle_RightButton_textview")
    logoutBtn=(By.ID,"com.tal.kaoyan:id/setting_logout_text")
    commit=(By.ID,"com.tal.kaoyan:id/tip_commit")


    def check_is_login(self):
        try:
            self.dr.find_element(*self.myself_loc).click()
            self.dr.find_element(*self.username_info)
        except:
            self.login_action('ILOVET','admin888')
        else:
            pass


    def login_action(self,username,password):
        logging.info("====start login====")
        self.dr.find_element(*self.myself_loc).click()
        self.dr.find_element(*self.login_loc).click()
        self.dr.find_element(*self.username_loc).send_keys(username)
        self.dr.find_element(*self.password_loc).send_keys(password)
        self.dr.find_element(*self.loginBtn).click()

    def logout(self):
        self.dr.find_element(*self.setting_loc).click()
        self.dr.find_element(*self.logoutBtn).click()
        self.dr.find_element(*self.commit).click()


    def check_login_status(self):
        logging.info('==check_login==')
        try:
            self.dr.find_element(*self.username_info)
        except:
            logging.error("login fail")
            self.getscreenshot('login fail')
            return False
        else:
            logging.info('login sucess')
            self.logout()
            return True

if __name__=="__main__":
    dr=appium_desired()
    l=LoginView(dr)
    l.login_action('ILOVET','admin888')
    l.check_login_status()






