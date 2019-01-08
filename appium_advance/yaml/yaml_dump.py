import yaml
#转为yaml数据格式
slogan=['huangguangchuang','ni','zhenchou']
website={'url':'www.baidu.com'}

print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))