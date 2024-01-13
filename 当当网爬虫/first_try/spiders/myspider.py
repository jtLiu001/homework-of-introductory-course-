import scrapy
import logging
from first_try.items import FirstTryItem


class MySpider(scrapy.Spider):
    name = 'Myspider'
    allowed_domains = ['dangdang.com']  # 修改为目标网站的域名
    start_urls = ['http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index=1']  # 修改为目标网站的URL

    def parse(self,response,**kwargs):
        bigimg=response.css('ul.bigimg')
        book_list=bigimg.css('ul li')
        for product in book_list:
            item=FirstTryItem()
            item['book_name']=product.css('a.pic::attr(title)').get()
            item['picture']=product.css('img::attr(src)').get()
            item['auther_name']=product.css('[dd_name="单品作者"]::text').get()
            item['Press']=product.css('[dd_name="单品出版社"]::text').get()
            price=product.css('span.search_now_price::text').get()
            item['price']=price.replace('&yen;', '').strip()
            item['hyperlink']=product.css('a.pic::attr(href)').get()
            yield item
        page_shift=response.css('[dd_name="底部翻页"]')
        if page_shift:
            next_page=page_shift.css('li.next a::attr(href)').get()
            pages=page_shift.css('li a.null::text').get()
            logging.info("pass here!!!!!")
            if next_page and int(pages) <100:
                yield response.follow(next_page,self.parse)
        # 提取数据，填充item对象
        # 例如：item['name'] = response.xpath('//h1/text()').extract_first()

