#!python3
from lxml import html
from lxml import etree
from string import printable
import requests
import re


res = requests.get('https://www.town.nishikatsura.yamanashi.jp/info/351')

print(res.text)
# f = html.fromstring(res.content.decode())

# print(content)
# f = open('./test/test.html')
# string = f.read()
# f.close()

# string = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', string)
# string = re.sub(r'\s', '', string)
# string = re.sub(r'<--.*-->', '', string)


# text = html.fromstring(string)

# print(string)

# print(text.xpath('//text()'))