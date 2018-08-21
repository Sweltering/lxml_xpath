from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html', parser=parser)

# 1、获取所有tr标签
# //tr
# trs = html.xpath('//tr')  # 返回一个列表
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))


# 2、获取第二个tr标签
# tr = html.xpath('//tr[2]')[0]
# print(etree.tostring(tr, encoding='utf-8').decode("utf-8"))


# 3、获取所有class等于even的tr标签
# trs = html.xpath('//tr[@class="even"]')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))


# 4、获取所有a标签的href属性的值
# aList = html.xpath('//a/@href')
# for a in aList:
#     print('https://hr.tencent.com/' + a)


# 5、获取所有的职位信息（纯文本）
# text()获取标签下的文本信息
trs = html.xpath('//tr[position()>1]')  # 第一个tr标签过滤掉
positions = []
for tr in trs:
    href = tr.xpath('.//a/@href')[0]  # .当前标签下的a标签
    fullurl = 'https://hr.tencent.com/' + href
    title = tr.xpath('./td[1]//text()')[0]
    category = tr.xpath('./td[2]/text()')
    nums = tr.xpath('./td[3]/text()')
    address = tr.xpath('./td[4]/text()')
    pubtime = tr.xpath('./td[5]/text()')

    position = {
        'url': fullurl,
        'title': title,
        'category': category,
        'nums': nums,
        'address': address,
        'pubtime': pubtime
    }
    positions.append(position)

print(positions)
