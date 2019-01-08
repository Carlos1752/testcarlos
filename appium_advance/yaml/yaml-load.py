import yaml
#从yaml数据提取出来
file=open('familyinfo.yaml')
data=yaml.load(file)

print(data)

print(data['name'])
print(data['age'])

print(data['spouse']['name'])
print(data['spouse']['age'])

# print(data['children'])  #打印出yaml文件中children所有的内容
print(data['children'][0]['name'])  #打印出children的第一个
print(data['children'][0]['age'])

print(data['children'][1]['name'])   #打印出第二个
print(data['children'][1]['age'])

data['name']='Carlos'
print(data['name'])


