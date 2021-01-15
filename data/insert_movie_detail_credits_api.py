# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper
from helper import db_helper

table_str_keys = ["id", "name", "url", "abstract", "cover_url", "latin_name", "title"]
table_str_keys_rel = ["movie_id", "celebrity_id", "role"]


def assemble_celebs(values):
    return f'''
            INSERT INTO 'celebrities' (
            {str.join(',', table_str_keys)}
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def assemble_rels(values):
    return f'''
            INSERT INTO 'movie_celebrities' (
            {str.join(',', table_str_keys_rel)}
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def insert_movie_celeb(db, data):

    for j in data:
        values = []
        for i in j.get('credits'):  # [:1]:
            values = []
            role = i['title']
            movie_id = j.get('meta')['id']
            for p in i.get('celebrities'):
                print(p.get('id'))
                val = str.join(',', map(lambda x: f'''"{db_helper.norm_str(p.get(x))}"''', table_str_keys))
                sql_insert = assemble_celebs([val])
                try:
                    db.execute(sql_insert)
                except Error as e:
                    print(e)

                values.append(f'''
                {movie_id},
                {p.get('id')},
                "{role}"
                ''')

        if len(values) > 0:
            sql_insert_rel = assemble_rels(values)
            try:
                db.execute(sql_insert_rel)
            except Error as e:
                print(e)

    db.commit()


def main():
    db = db_helper.create_connection()
    data = helper.read_json('movie_detail_credits_api')
    insert_movie_celeb(db, data)
    db_helper.close_connection(db)


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python db_helper.py tablename')
    # else:
    #     house = args[1]
    main()
