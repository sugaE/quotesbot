# QuotesBot
Get my douban collect list data.

## Folders
- data: store data
- helper: utils
- mock: localized website data for debug use.
- quotesbot: crawlers 

## Extracted data

Data first saved in JSON then in sqlite database.

To restort the database, execute `create_db.py` in data folder:


## Useful commands

```shell script
# list all the scrapy available
scrapy list 

# execute and output
scrapy crawl toscrape-css -o quotes.json
```


## Useful links
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html)

