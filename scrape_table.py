#encoding: utf-8
"""
Scrape the table from the website www.qctsw.com
"""

from lxml.html import parse

def scrape_a_page(page):
    """
    Scrape a table from the page
    """
    doc = parse(page).getroot()
    header = ["投诉编号", "投诉品牌", "投诉人", "投诉时间", "4S店名称", "投诉时间",
            "4S店联系人", "投诉地区", "4S店电话", "所属车型", "车辆状态",
            "购车时间", "里程数", "投诉问题", "投诉诉求"]
    print ",".join(header)
    i = 1
    for link in doc.cssselect('td'):
        i += 1
        if i % 2:
            print "".join(link.text_content().split()) + ",",

if __name__ == "__main__":
    #Range starts at 6000
    for i in range(6000, 6003):
        template = 'http://www.qctsw.com/tousu/content/%d.html'
        scrape_a_page(template % i)
