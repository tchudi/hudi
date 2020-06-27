from appium import webdriver

def capability():
    desired_caps = {'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'3.9',
                    'appPackage':'com.tal.kaoyan',
                    'appActivity':'.ui.activity.HomeTabActivity',
                    "unicodeKeyboard":'True',   # 使用 unicodeKeyboard 的编码方式来发送字符串
                    "resetKeyboard":'True'      # 将键盘给隐藏起来
                    }
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver


def capability1():
    desired_caps = {'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'3.9',
                    'appPackage':'com.wondershare.drfone',
                    'appActivity':'com.wondershare.drfone',
                    "unicodeKeyboard":'True',   # 使用 unicodeKeyboard 的编码方式来发送字符串
                    "resetKeyboard":'True'      # 将键盘给隐藏起来
                    }
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver


def capability2():
    desired_caps = {'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'3.9',
                    'appPackage':'com.mymoney',
                    'appActivity':'com.mymoney.biz.splash.SplashScreenActivity',
                    "unicodeKeyboard":'True',   # 使用 unicodeKeyboard 的编码方式来发送字符串
                    "resetKeyboard":'True'      # 将键盘给隐藏起来
                    }
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver

def capability3():
    desired_caps = {'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'3.9',
                    'appPackage':'com.baidu.BaiduMap',
                    'appActivity':'com.baidu.baidumaps.MapsActivity',
                    "unicodeKeyboard":'True',   # 使用 unicodeKeyboard 的编码方式来发送字符串
                    "resetKeyboard":'True'      # 将键盘给隐藏起来
                    }
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver
