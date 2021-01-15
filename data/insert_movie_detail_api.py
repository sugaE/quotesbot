# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper
from helper import db_helper

table_str_keys = ["status", "create_time", "comment"]
table_num_keys = ["id"]
table_arr_keys = ["tags"]
table_else_keys = ["movie_id", "rating"]


def assemble_movies(values):
    return f'''
            INSERT INTO 'my_collect' (
            {str.join(',', table_str_keys + table_num_keys + table_arr_keys + table_else_keys)}
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def insert_my_collect(db, data):
    values = []
    for y in data:  # [:1]:
        p = y.get('interest')
        if p:
            val = ''
            val += str.join(',', map(lambda x: f'''"{db_helper.norm_str(p.get(x))}"''', table_str_keys)) + ','
            val += str.join(',', map(lambda x: f'{p.get(x)}', table_num_keys)) + ','
            val += str.join(',', map(lambda x: f'''"{str.join(',', p[x])}"''' if p.get(x) else 'NULL', table_arr_keys)) + ','

            # "movie_id"
            if y.get('id'):
                val += f'''"{y['id']}",'''
            else:
                val += 'NULL,'

            # "rating"
            if p.get('rating'):
                val += f'''{p['rating'].get('value', 0)}'''
            else:
                val += 'NULL'

            values.append(val)

            if len(values) >= 10:
                sql_insert = assemble_movies(values)
                values.clear()
                print(sql_insert)
                db.execute(sql_insert)

    if len(values) > 0:
        sql_insert = assemble_movies(values)
        print(sql_insert)
        db.execute(sql_insert)
    db.commit()


def main():
    db = db_helper.create_connection()
    data = helper.read_json('movie_detail_api')
    insert_my_collect(db, data)
    db_helper.close_connection(db)


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python db_helper.py tablename')
    # else:
    #     house = args[1]
    main()
