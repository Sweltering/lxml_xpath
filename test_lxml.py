from lxml import etree

# 1、通过文本解析html
text = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="1" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="1 square">
                <a target="_blank"
                   href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">
                    22989-金融云区块链高级研发工程师（深圳）
                </a>
            </td>  
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2018-08-21</td>
        </tr>
        <tr class="odd">
            <td class="1 square">
                <a target="_blank" 
                href="position_detail.php?id=29938&amp;keyword=python&amp;tid=87&amp;lid=2218">
                    22989-金融云高级后台开发
                </a>
            </td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2018-08-21</td>
        </tr>
        <tr class="odd">
            <td class="1 square">
                <a target="_blank" 
                href="position_detail.php?id=29938&amp;keyword=python&amp;tid=87&amp;lid=2218">
                    15851-后台开发工程师
                </a>
            </td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2018-08-21</td>
        </tr>
        <tr class="odd">
            <td class="1 square">
                <a target="_blank" 
                href="position_detail.php?id=29938&amp;keyword=python&amp;tid=87&amp;lid=2218">
                    SNG11-高级业务运维工程师（深圳）
                </a>
            </td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2018-08-21</td>
        </tr>
    </tbody>
</table>
"""


def parse_text():
    html = etree.HTML(text)  # 返回一个lxml.etree._Element对象
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

# 2、从文件中读取html代码
def parse_tencent_file():
    html = etree.parse('tencent.html')
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

# 有些HTML可能不规范，导致解析失败，需要指定解析器parser
def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')   # HTMLParser解析器
    html = etree.parse('lagou.html', parser=parser)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    # parse_text()
    # parse_tencent_file()
    parse_lagou_file()