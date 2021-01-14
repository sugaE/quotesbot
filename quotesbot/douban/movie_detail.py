# -*- coding: utf-8 -*-
# @author Wendy
# @created on 2021/1/13
import scrapy
from scrapy.selector import Selector
import helper

# https://m.douban.com/rexxar/api/v2/tv/27157689?ck=lvDn&for_mobile=1
# https://m.douban.com/rexxar/api/v2/tv/27157689/credits
# https://m.douban.com/rexxar/api/v2/tv/27157689/rating?ck=lvDn&for_mobile=1


class ToScrapeMovieDetail(scrapy.Spider):
    name = 'douban_movie_detail'
    start_urls = list(map(lambda x: x["link"], helper.read_json('my_collect')))[:1]

    def parse(self, response):
        res = parse_body(response)
        yield res


def parse_body(response):
    # for quote in response.css('.subjectwrap .info'):
    #     info = quote.css('.info')
    #     titlestr = info.css('.title em').xpath('.//text()').extract_first()
    #     tagstr = info.css('.intro').xpath('.//text()').extract_first()

    res = {}
    rating_w = response.css('.rating_wrap')
    res['rating_avg'] = rating_w.css('[property="v:average"]::text').get()
    res['rating_num'] = rating_w.css('[property="v:votes"]::text').get()
    ratings = rating_w.css('.rating_per::text').getall()
    if len(ratings) > 0:
        for i, x in enumerate(ratings):
            res['rating_' + str(5 - i)] = x[:-1] if str.endswith(x, '%') else 0

    mark_w = response.css('.j.a_stars')
    res['mark'] = mark_w.css('#n_rating').attrib['value']
    res['mark_date'] = mark_w.css('.collection_date::text').get()
    comment = mark_w.css('span:last-child')
    if not comment.attrib['id']:
        res['mark_comment'] = comment.css('::text').get()

    return res


def main():
    body = helper.read_mock('movie_detail')
    response = Selector(text=body)
    res = parse_body(response)
    print('[yield]', res)


if __name__ == '__main__':
    main()
