#此脚本说明通过脚本调用desired_caps.yaml的参数，如果需要修改手机参数，则在yaml中修改即可
from appium import webdriver
import yaml

file=open('desired_caps.yaml','r')
data=yaml.load(file)

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

driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)