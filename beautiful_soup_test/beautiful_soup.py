from bs4 import BeautifulSoup
import re

html_doc = '/Users/prinsterfanz/Downloads/kokodayo.html'
html_file = open(html_doc, 'r', encoding='UTF-8')
html_handle = html_file.read()
soup = BeautifulSoup(html_handle, 'html.parser')

# 获取html头信息
# print(soup.p)

# 获取节点中的属性
# print(soup.p.attrs)

# ps = soup.find_all('p')
# print(ps)

# 按照id进行搜索
# result = soup.find_all(id="and_button")
# print(result)

# 按照css进行搜索
# title = soup.find_all('div')
# print(title)

# reg = ">(\w*)</a>"
# result = re.findall(reg, str(title))
# print(result)

result = soup.find_all('label')
print(result)
