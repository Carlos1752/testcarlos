# coding:utf-8

import time
import os
import re
import yaml
import logging
import logging.config

from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction

file=open('desired_caps.yaml','r') #引入yaml参数表
data=yaml.load(file)

# logging.basicConfig(level=logging.DEBUG,filename='runlog.log',
#                     format='%(asctime)s  --%(filename)s  --[line:%(lineno)d]  --%(levelname)s  --%(message)s')  #打印出时间、行数、信息

CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

desired_caps={}
desired_caps['platformName']=data['platformName']
desired_caps['deviceName']=data['deviceName']
desired_caps['platforVsersion']=data['platforVsersion']
desired_caps['uuid']=data['uuid']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']

desired_caps['noReset']=data['noReset']
desired_caps['unicodeKeyvboard']=data['unicodeKeyvboard']
desired_caps['resetKeyboard']=data['resetKeyboard']

logging.info('start app...')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)

logging.info('开始读取机型信息')
os.system('adb version')
os.system('adb devices')  # os.system是不支持读取操作的
# out = os.popen('adb uninstall com.tencent.tws.gdevicemanager').read()  # os.popen支持读取操作
# print(out)
# out = os.popen('adb reboot').read()  # os.popen支持读取操作

logging.info('卸载成功...')

#下面的代码是获取当前窗口的component参数
def getFocusedPackageAndActivity():
    pattern = re.compile(
        r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")  # 这里使用了正则表达式，对输出的内容做了限制，只会显示类似"com.mediatek.factorymode/com.mediatek.factorymode.FactoryMode"的字符串
    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()  # window下使用findstr
    list = pattern.findall(out)
    component = list[0]  # 输出列表中的第一条字符串

    return component

# print(getFocusedPackageAndActivity())

time.sleep(5)
# driver.keyevent(3)
driver.close_app()
logging.info('关闭APP...')
time.sleep(5)
driver.launch_app()
logging.info('启动APP...')
time.sleep(5)

driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/qqLoginView').click()
time.sleep(2)
driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/button2').click()  #取消弹框（ID方式）
# driver.find_element_by_xpath('//*[@class="android.widget.Button" and @index="0"]').click() #取消弹框（xpath方式）
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/qqLoginView').click()
time.sleep(2)
driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/button1').click()  #取消弹框（ID方式）
time.sleep(2)
# 点击普通下载按钮
driver.tap([(105,370),(106,380)], 500)  #分辨率为1080*1920的手机
time.sleep(100)
driver.tap([(807,448),(807,450)], 500)


# driver.find_element_by_id('com.qiku:id/permission_remember_choice_checkbox').click()
# time.sleep(1)
# driver.find_element_by_id('android:id/button1').click()
#
# time.sleep(3)
#
# # 点击登录按钮
# driver.tap([(981,866),(999,986)], 500)  #分辨率为1080*1920的手机





