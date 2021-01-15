# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper


def get_split_arr(tagstr):
    tags = None
    if tagstr is not None:
        tags = str.split(tagstr, '/')
        tags = list(map(lambda x: str.strip(x), tags))
    return tags


def norm_str(strr):
    return str.replace(strr, '"', '""')


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(helper.proj_dir, 'data', 'quotesbot.db'))
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn


def close_connection(conn):
    if conn:
        conn.close()


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python db_helper.py tablename')
    # else:
    #     house = args[1]
    print('[db_helper]')
