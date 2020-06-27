from businessView.loginView import LoginView
from selenium.webdriver.common.by import By
import logging
from common.desired_caps import appium_desired

class ForumView(LoginView):
    forum_loc=(By.ID,"com.tal.kaoyan:id/mainactivity_button_forum")
    forum_title=(By.ID,"com.tal.kaoyan:id/hot_thread_item_title")
    commenttip=(By.ID,"com.tal.kaoyan:id/activity_threaddetail_commenttip_btn")
    text=(By.ID,"com.tal.kaoyan:id/createthread_insertimg_imgslayout")
    send=(By.ID,"com.tal.kaoyan:id/createthread_title_send")
    enter=(By.ID,"android:id/button1")

    def forum_send(self):
        self.dr.find_element(*self.forum_loc).click()
        self.dr.find_element(*self.forum_title).click()
        self.dr.find_element(*self.commenttip).click()
        self.dr.find_element(*self.text).send_keys('111111')
        self.dr.find_element(*self.send).click()
    def forum_send_status(self):
        try:
            ele=self.dr.find_element(*self.enter)
        except:
            logging.info('fail')
            return False
        else:
            logging.info('sucess')
            ele.click()
            return True



if __name__=="__main__":
    dr=appium_desired()
    f=ForumView(dr)
    f.forum_send()
    f.forum_send_status()

