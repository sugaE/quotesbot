# import json to sqlite db

import sqlite3
from sqlite3 import Error
import os
import helper
from helper import db_helper


def assemble_insert(values):
    return f'''
            INSERT INTO "movies" (
            id, cover_url, original_title, title, url, release_date, release_region
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def insert_table(db, data):
    # db.execute(f'''
    # delete from '{table_name}'
    # ''')

    values = []
    for p in data:  # [:1]:
        titles = p['titles']
        titles.reverse()
        link = p['link']
        date = p['date']
        date_region = str.split(date, '(')

        values.append(f'''
            "{str.split(link, '/')[-2]}",
            "{p['image']}",
            "{db_helper.norm_str(titles[0])}",
            "{titles[1] if len(titles) > 1 else ''}",
            "{link}",
            "{date_region[0]}",
            "{date_region[-1][:-1] if len(date_region) > 1 else ''}"
        ''')

        if len(values) >= 15:
            sql_insert = assemble_insert(values)
            values.clear()
            print(sql_insert)
            db.execute(sql_insert)

    if len(values) > 0:
        sql_insert = assemble_insert(values)
        print(sql_insert)
        db.execute(sql_insert)
    db.commit()


def create_table(db, table_name):
    # sql_utf = '''
    #     ALTER DATABASE
    # database_name
    # CHARACTER SET = utf8mb4
    # COLLATE = utf8mb4_unicode_ci;
    #     '''
    # db.execute(sql_utf)
#
    try:
        db.execute(f'''DROP TABLE "{table_name}"''')
    except Error as e:
        print(e)

    sql_create = f'''

'''

    db.execute(sql_create)


def main():
    db = db_helper.create_connection()
    data = helper.read_json()
    insert_table(db, data)
    db_helper.close_connection(db)


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python db_helper.py tablename')
    # else:
    #     house = args[1]
    main()
