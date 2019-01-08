import time
import os
import re
import yaml
import logging
import logging.config

from appium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait

file=open('../yaml/desired_caps.yaml','r') #引入yaml参数表
data=yaml.load(file)

# logging.basicConfig(level=logging.DEBUG,filename='runlog.log',
#                     format='%(asctime)s  --%(filename)s  --[line:%(lineno)d]  --%(levelname)s  --%(message)s')  #打印出时间、行数、信息

CON_LOG='../yaml/log.conf'
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

logging.info('click 协议...')

time.sleep(6)

driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/protocolTextView').click()
driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/action_mode_close_button').click()
time.sleep(2)
# driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/qqLoginView').click()
# time.sleep(2)
# driver.find_element_by_xpath('//android.widget.Button').click()
# driver.find_element_by_class_name('android.widget.TextView').click()

logging.info('点击手机号登录...')
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/msgLoginView').click() #点击手机号登录
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginPwdLinkTxt').click()#点击切换到密码登录
time.sleep(1)
logging.info('切换到验证码登录...')
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginPwdLinkTxt').click()#点击切换到验证码登录
logging.info('返回到登录首页...')
driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/action_mode_close_button').click()#点击取消，返回到登录首页
time.sleep(3)
logging.info('点击手机号登录...')
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/msgLoginView').click()#点击手机号登录
logging.info('切换到密码登录...')
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginPwdLinkTxt').click()#点击切换到密码登录
time.sleep(5)
logging.info('开始输入账号密码...')
driver.find_element_by_class_name('android.widget.TwsEditText').send_keys('13267101427')#输入手机号
driver.find_element_by_xpath('//android.widget.TwsEditText[@text="输入登录密码"]').send_keys('huang123456') #输入密码
time.sleep(2)
# 点击眼睛按钮
driver.tap([(958,577),(960,576)], 500)  #分辨率为1080*1920的手机
time.sleep(2)
driver.save_screenshot('login.png')   #截图到脚本目录
driver.get_screenshot_as_file('../yaml/login.png') #截图到指定目录

logging.info('点击登录...')
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginNextStepBtn').click()  #点击登录按钮
time.sleep(2)
logging.info('登录成功...')

image=driver.find_elements_by_class_name('android.widget.TextView') #通过list方式点击选择设备类型
image[1].click()

time.sleep(5)
WebDriverWait(driver,1).until(lambda x:x.find_element_by_id('com.tencent.tws.gdevicemanager:id/choose_list'))  #元素等待
driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout" and @index="0"]').click() #使用xpath方式点击渤海设备类型

logging.info('点击渤海P1')
logging.info('提示绑定微信运动')

time.sleep(15)
driver.find_element_by_id('com.tencent.tws.phoneside.common.healthkit:id/btn_bind_wx_sports_later').click() #点击暂不绑定

driver.find_element_by_class_name('android.widget.RelativeLayout').click() #点击进入闹钟管理
logging.info('进入闹钟管理界面')
driver.find_element_by_id('android:id/home').click()
driver.find_element_by_xpath('//android.widget.TextView[@text="微信支付"]').click()#点击微信支付
logging.info('进入微信支付界面')
time.sleep(2)
driver.find_element_by_id('com.pacewear.wechatpay.phoneside:id/auth_now').click()#点击立即开通
time.sleep(5)
# logging.info('进入授权界面')

#获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y
l=get_size()
print(l)

#从下往上拖动4次
def swipeLeft():
    l=get_size()
    y1=int(l[0]*0.9)
    x1=int(l[1]*0.5)
    y2=int(l[0]*0.1)
    driver.swipe(x1,y1,x1,y2,1000)

for i in range(4):
    swipeLeft()
    sleep(1) #每次等待1秒

print(i)  #打印次数