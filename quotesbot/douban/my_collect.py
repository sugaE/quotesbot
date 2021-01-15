# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals

domaindb = 'https://movie.douban.com'


def getArr(tagstr):
    tags = None
    if tagstr is not None:
        tags = str.split(tagstr, '/')
        tags = list(map(lambda x: str.strip(x), tags))
    return tags


class ToScrapeSpiderMyCollect(scrapy.Spider):
    name = 'douban_my_collect'
    start_urls = [
        domaindb + '/people/sugae/collect' #+ pg_num
    ]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ToScrapeSpiderMyCollect, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.engine_stopped, signal=signals.engine_stopped)
        return spider

    def parse(self, response):
        for quote in response.css('.grid-view .item'):
            info = quote.css('.info')
            titlestr = info.css('.title em::text').extract_first()
            tagstr = info.css('.intro::text').extract_first()
            tags = getArr(tagstr)
            link = info.css('.title a').attrib['href']
            mid = str.split(link, '/')[-2]

            yield {
                'image': quote.css('.nbg img').attrib['src'],
                'titles': getArr(titlestr),
                'link': link,
                'tags': tags[1:] if tags is not None and len(tags) > 1 else None,
                'date': tags[0] if tags is not None else ''
            }

        next_page_url = response.css('.paginator .next a').attrib['href']
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(domaindb + next_page_url))

    def engine_stopped(self):
        print('engine_stopped')


