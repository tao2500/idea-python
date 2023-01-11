from urllib import request
from bs4 import BeautifulSoup


req = request.Request("http://www.news.cn/world/2022-11/19/c_1129141540.htm")
response = request.urlopen(req)
# 获取返回信息
html = response.read()
# 解码
html = html.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# 标题
title = soup.title.string
print(title)
# 正文
content1 = soup.find_all('p')[3].string
content2 = soup.find_all('p')[4].string
content = content1 + content2
print(content1)
print(content2)
# 来源
url = "URL:"+response.geturl()
print(url)
# print(soup.prettify())
# 发布日期/来源
date = soup.select_one(".info").get_text()
print(date)
# 责任编辑
auto = soup.select_one(".editor").string
print(auto)
# 存储到new.txt中
file = open('new.txt', 'w')
file.write(title+content+url+date+auto)
print("写入new.txt完成")
