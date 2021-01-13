#
import requests


def main():
    # https://www.douban.com/j/doulist/cat?limit=8&start=0
    url = 'https://www.douban.com/j/doulist/134789934/additem'
    data = {
        'sid': 2340927,  # 资源id
        'skind': 1002,  # 电影分类
        'comment': '',
        'ck': 'lvDn'
    }
    r = requests.post(url, data)
    print(r.status_code, r.reason)


if __name__ == '__main__':
    main()
