# -*- coding: utf-8 -*-
# @author Wendy
# @created on 2021/1/13
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import helper
import json

# https://m.douban.com/rexxar/api/v2/tv/27157689?ck=lvDn&for_mobile=1
# https://m.douban.com/rexxar/api/v2/tv/27157689/credits
# https://m.douban.com/rexxar/api/v2/tv/27157689/rating?ck=lvDn&for_mobile=1


class ToScrapeMovieDetailApi(scrapy.Spider):
    name = 'douban_movie_detail_api'

    def start_requests(self):
        for x in get_start_ids():
            yield Request(f'https://m.douban.com/rexxar/api/v2/movie/{x}?ck=lvDn&for_mobile=1',
                          cookies=helper.cookies,
                          )

    def parse(self, response):
        res = parse_body(response)
        yield res


def get_start_ids():
    data = helper.read_json('my_collect')
    crawled = helper.read_json('movie_detail_api')
    return filter(lambda y: y not in map(lambda x: x['id'], crawled), map(lambda x: str.split(x['link'], '/')[-2], data))


def parse_body(response):
    return json.loads(response.text)


def main():
    body = helper.read_mock('movie_detail_api')
    res = parse_body(body)
    print('[yield]', res)


if __name__ == '__main__':
    main()
