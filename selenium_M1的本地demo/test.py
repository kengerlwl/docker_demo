import time
from selenium import webdriver


# 打开指定网页，
driver = webdriver.Firefox(executable_path = './geckodriver')
driver.get("https://space.bilibili.com/10330740/search/dynamic?keyword=%E4%BF%84%E4%B9%8C")


# 手动操作登录获取cookie
time.sleep(100)



# 获取cookie
cookie_list=driver.get_cookies()
cookie_str =";".join([item["name"] +":" + item["value"] +"" for item in cookie_list])

cookies={}#初始化cookies字典变量
for line in cookie_str.split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容



# 使用requests进行爬取数据
ans = []
import requests
# 根据页数不同开始遍历
for i in range(1,30):
    url = "https://api.bilibili.com/x/space/dynamic/search?keyword=俄乌&mid=10330740&pn={}&ps=30&platform=web".format(i)
    res=requests.get(url,cookies=cookies)
