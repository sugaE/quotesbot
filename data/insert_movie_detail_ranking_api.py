# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper
from helper import db_helper

table_num_keys = ["wish_count", "doing_count", "done_count"]
table_else_keys = ["stats_5", "stats_4", "stats_3", "stats_2", "stats_1"]


def insert_ranking(db, data):
    for p in data:  # [:1]:
        stats = p.get('stats')
        meta = p.get('meta')
        if meta and stats:
            sql_update = f'''
                UPDATE 'movies' SET 
                wish_count = {p.get('wish_count')},
                doing_count = {p.get('doing_count')},
                done_count = {p.get('done_count')},
                stats_5 = {stats[4]},
                stats_4 = {stats[3]},
                stats_3 = {stats[2]},
                stats_2 = {stats[1]},
                stats_1 = {stats[0]}
                WHERE id="{meta['id']}"'''
            db.execute(sql_update)
    db.commit()


def main():
    db = db_helper.create_connection()
    data = helper.read_json('movie_detail_ranking_api')
    insert_ranking(db, data)
    db_helper.close_connection(db)


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python db_helper.py tablename')
    # else:
    #     house = args[1]
    main()
