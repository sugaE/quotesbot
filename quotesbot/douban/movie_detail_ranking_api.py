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
    name = 'douban_movie_detail_ranking_api'
    # start_urls = [
    #     'https://m.douban.com/rexxar/api/v2/tv/27157689?ck=lvDn&for_mobile=1'
    # ]

    def start_requests(self):
        for x in get_start_ids():
            yield Request(f'https://m.douban.com/rexxar/api/v2/{x["type"]}/{x["id"]}/rating?ck=lvDn&for_mobile=1',
                          cookies=helper.cookies,
                          meta=dict(x=x)
                          )

    def parse(self, response):
        res = parse_body(response)
        yield res


def get_start_ids():
    data = helper.read_json('movie_detail_api')
    return map(lambda x: {'id': x['id'], 'type': x['type']}, data)


def parse_body(response):
    res = json.loads(response.text)
    if (not res.get('meta')) and response.meta and response.meta.get('x'):
        res['meta'] = response.meta['x']
    return res


def main():
    body = helper.read_mock('movie_detail_ranking_api')
    print('[yield]', body)


if __name__ == '__main__':
    main()
