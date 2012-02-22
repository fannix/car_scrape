"""
Scrape the table from the website www.qctsw.com
"""

from lxml.html import parse

def scrape_a_page(page):
    """
    Scrape a table from the page
    """
    doc = parse(page).getroot()

    for link in doc.cssselect('td'):
        print "".join(link.text_content().split())

if __name__ == "__main__":
    #Range starts at 6000
    for i in range(6000, 6003):
        template = 'http://www.qctsw.com/tousu/content/%d.html'
        scrape_a_page(template % i)
