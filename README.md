# QuotesBot
Get my douban collect list data.

## Folders
- data: store data
- helper: utils
- mock: localized website data for debug use.
- quotesbot: crawlers 

## Extracted data

Data first saved in JSON then in sqlite database.

Current execute order is:

0. createTables.sql
1. insert_movie_detail_api.py
2. insert_movie_detail_ranking_api.py
3. insert_movie_detail_credits_api.py
4. insert_my_collect_api.py

## Useful commands

```shell script
# list all the scrapy available
scrapy list 

# execute and output
scrapy crawl toscrape-css -o quotes.json
```


## Useful links
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html)

