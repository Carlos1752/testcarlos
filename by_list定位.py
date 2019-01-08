import time
import sys
# sys.path.append('path')
import os
import re
from time import sleep
from capability import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/msgLoginView').click()  #点击手机号登录
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginPwdLinkTxt').click() #点击切换到密码登录
driver.find_element_by_class_name('android.widget.TwsEditText').send_keys('13267101427') #输入手机号码
driver.find_element_by_xpath('//android.widget.TwsEditText[@text="输入登录密码"]').send_keys('huang123456') #输入密码
driver.find_element_by_id('com.pacewear.tws.phoneside.plugin.login:id/loginNextStepBtn').click()  #点击登录按钮
time.sleep(10)
image=driver.find_elements_by_class_name('android.widget.TextView') #通过list方式点击选择设备类型
image[1].click()

WebDriverWait(driver,1).until(lambda x:x.find_element_by_id('com.tencent.tws.gdevicemanager:id/choose_list'))  #元素等待
driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout" and @index="0"]').click() #使用xpath方式点击渤海设备类型

time.sleep(2)
#获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y
l=get_size()
print(l)

time.sleep(5)
driver.find_element_by_id('com.tencent.tws.phoneside.common.healthkit:id/btn_bind_wx_sports_later').click() #点击暂不绑定
driver.find_element_by_class_name('android.widget.RelativeLayout').click() #点击进入闹钟管理
driver.find_element_by_id('android:id/home').click()
driver.find_element_by_xpath('//android.widget.TextView[@text="微信支付"]').click()#点击微信支付
time.sleep(2)
# driver.find_element_by_id('com.pacewear.wechatpay.phoneside:id/auth_now').click()#点击立即开通
# time.sleep(5)
# driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/tv_bottom_button').click() #点击立即创建
# time.sleep(5)
# driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/scv_edittext').send_keys(1234)#输入密码1234
# time.sleep(5)
# driver.find_element_by_id('com.tencent.tws.gdevicemanager:id/scv_edittext').send_keys(1234)#输入确认密码1234
driver.find_element_by_id('com.pacewear.wechatpay.phoneside:id/tv_left_top_cancel').click()#点击取消按钮

driver.find_element_by_xpath('//*[@class="android.widget.FrameLayout" and @index="1"]').click()


# #从下往上拖动4次
# def swipeLeft():
#     l=get_size()
#     y1=int(l[0]*0.9)
#     x1=int(l[1]*0.5)
#     y2=int(l[0]*0.1)
#     driver.swipe(x1,y1,x1,y2,1000)
#
# for i in range(4):
#     swipeLeft()
#     sleep(1) #每次等待1秒
#
# print(i)  #打印次数