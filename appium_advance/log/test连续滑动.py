import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='360手机 N5'
desired_caps['platforVsersion']='7.1.1'
desired_caps['uuid']='c23d076'

desired_caps['appPackage']='com.android.gallery3d'  #打开手机图库
desired_caps['appActivity']='com.android.gallery3d.app.Gallery'  #打开手机图库
desired_caps['noReset'] = 'True'
desired_caps['unicodeKeyvboard'] = "True"
desired_caps['resetKeyboard'] = "True"

# logging.info('start app...')
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

driver.tap([(143,469),])  #点击左上角第一张图片
time.sleep(3)

def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y
l=get_size()
print(l)

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']


def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    pinch_action=MultiAction(driver)

    action1.press(x=x * 0.3, y=y * 0.3).wait(2000).move_to(x=x * 0.5, y=y * 0.5).wait(2000).release()
    action2.press(x=x * 0.7, y=y * 0.7).wait(2000).move_to(x=x * 0.5, y=y * 0.5).wait(2000).release()

    pinch_action.add(action1,action2)
    print('start pinch...')
    pinch_action.perform()


def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.5, y=y * 0.5).wait(1000).move_to(x=x * 0.3, y=y * 0.3).wait(1000).release()
    action2.press(x=x * 0.7, y=y * 0.7).wait(1000).move_to(x=x * 0.9, y=y * 0.9).wait(1000).release()

    zoom_action.add(action1, action2)
    print('start zoom...')
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        zoom()
