from appium import webdriver
import logging
import logging.config


CON_LOG=r'D:/kyb_ui/config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def appium_desired():
    desired_caps = {'platformName': 'Android',
                    'deviceName': '127.0.0.1:62001',
                    'platformVersion': '3.9',
                    'appPackage': 'com.tal.kaoyan',
                    'appActivity': '.ui.activity.HomeTabActivity',
                    "unicodeKeyboard": 'True',  # 使用 unicodeKeyboard 的编码方式来发送字符串
                    "resetKeyboard": 'True'  # 将键盘给隐藏起来
                    }
    logging.info('----start app----')
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    dr.implicitly_wait(20)
    return dr

if __name__=='__main__':
    appium_desired()