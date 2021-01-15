# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper
from helper import db_helper

table_str_keys = ["id", "cover_url", "original_title", "title", "url", "type", "subtype", "intro"]
 # "stats_5", "stats_4", "stats_3", "stats_2", "stats_1", "wish_count", "doing_count", "done_count",
table_num_keys = ["episodes_count", "comment_count", "review_count"]
table_bit_keys = ["is_released", "is_restrictive", "is_show", "is_tv"]
table_arr_keys = ["genres", "countries", "languages", "durations"]
table_else_keys = ["rating_value", "rating_count", "pub_date", "pub_region", "tags"]


def assemble_movies(values):
    return f'''
            INSERT INTO 'movies' (
            {str.join(',', table_str_keys + table_num_keys + table_bit_keys + table_arr_keys + table_else_keys)}
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def assemble_tags(values):
    return f'''
            INSERT INTO 'tags' (
            id, name
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def assemble_alias(values):
    return f'''
            INSERT INTO 'movie_alias' (
            movie_id, alia
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def extract_tags(db, tags):
    ids = []
    for x in tags:
        tag_id = str.split(x['uri'], '/')[-1]
        ids.append(tag_id)
        val = f'''
        "{tag_id}",
        "{x['name']}"
        '''
    # if len(values) > 0:
        sql_insert = assemble_tags([val])
        try:
            db.execute(sql_insert)
        except Error as e:
            print(e, tag_id)
    return str.join(',', ids)


def extract_alias(db, movie_id, alias):
    values = []
    for i in alias:
        values.append(f'''
        "{movie_id}",
        "{db_helper.norm_str(i)}"
        ''')
    if len(values) > 0:
        sql_insert = assemble_alias(values)
        db.execute(sql_insert)


def insert_my_collect(db, data):
    values = []
    for p in data:  # [:1]:
        val = ''
        val += str.join(',', map(lambda x: f'''"{db_helper.norm_str(p.get(x))}"''', table_str_keys)) + ','
        val += str.join(',', map(lambda x: f'{p.get(x)}', table_num_keys)) + ','
        val += str.join(',', map(lambda x: '1' if p.get(x) else '0', table_bit_keys)) + ','
        val += str.join(',', map(lambda x: f'''"{str.join(',', p[x])}"''' if p.get(x) else 'NULL', table_arr_keys)) + ','

        # "rating_value", "rating_count",
        if p.get('rating'):
            val += f'''{p['rating'].get('value')},'''
            val += f'''{p['rating'].get('count')},'''
        else:
            val += 'NULL, NULL,'

        # "pub_date", "pub_region",
        if p.get('pubdate'):
            date_region = str.split(p.get('pubdate')[0], '(')
            val += f'''"{date_region[0]}",'''
            val += f'''"{date_region[-1][:-1] if len(date_region) > 1 else ''}",'''
        else:
            val += 'NULL, NULL,'

        # "tags"
        tags = extract_tags(db, p.get('tags'))
        val += f'"{tags}"'
        values.append(val)

        extract_alias(db, p.get('id'), p.get('aka'))

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


def insert_my_collect(db, data):
    print('my_collcet')


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
