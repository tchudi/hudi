# from appium import webdriver
# from time import sleep
#
# desired_caps = {'platformName':'Android',
#                 'deviceName':'127.0.0.1:62001',
#                 'platformVersion':'3.9',
#                 'appPackage':'com.tal.kaoyan',
#                 'appActivity':'.ui.activity.HomeTabActivity'
#                 }
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# dr.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
# dr.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_logintip_img").click()
# dr.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("admin888")
#
# dr.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").clear()
# dr.close_app()
# sleep(5)
# print(dr.page_source)
# views=dr.contexts
# print(views)
# print(dr.get_window_size())
# # print(dr.current_context)
# # print(dr.current_activity)
#
# dr.swipe(700,1200,700,200)

import random
def DaLeTou():
    print("109期大乐透中奖号码为：",end="")
    for i in range(5):
        print(random.randint(1,35),end=" ")
    print("+ ",end='')
    for i in range(2):
        print(random.randint(1,12),end=" ")

# def DoubleColorBall():
#     print("双色球中奖号码为：",end='')
#     for i in range(6):
#         print(random.randint(1,33),end='')
#     print("+ ",random.randint(1,16))
# DoubleColorBall()
DaLeTou()


