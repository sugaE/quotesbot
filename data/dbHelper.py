# import json to sqlite db

import sys
import sqlite3
from sqlite3 import Error
import os
import json


dir_path = os.path.dirname(os.path.realpath(__file__))


def open_json(table_name):
    with open(os.path.join(dir_path, table_name + '.json')) as json_file:
        data = json.load(json_file)
    return data


def get_split_arr(tagstr):
    tags = None
    if tagstr is not None:
        tags = str.split(tagstr, '/')
        tags = list(map(lambda x: str.strip(x), tags))
    return tags


def assemble_insert(table_name, values):
    return f'''
            INSERT INTO '{table_name}' (
            id, image, title, title_cn, url, release_date, release_region
            ) VALUES {str.join(', ',  map(lambda x: f'({x})', values))}'''


def norm_str(strr):
    return str.replace(strr, '"', '""')


def insert_table(db, table_name, data):
    db.execute(f'''
    delete from '{table_name}'
    ''')

    values = []
    for p in data:#[:1]:
        titles = p['titles']
        titles.reverse()
        link = p['link']
        date = p['date']
        date_region = str.split(date, '(')

        values.append(f'''
            "{str.split(link, '/')[-2]}",
            "{p['image']}",
            "{norm_str(titles[0])}",
            "{titles[1] if len(titles) > 1 else ''}",
            "{link}",
            "{date_region[0]}",
            "{date_region[-1][:-1] if len(date_region) > 1 else ''}"
        ''')

        if len(values) >= 15:
            sql_insert = assemble_insert(table_name, values)
            values.clear()
            print(sql_insert)
            db.execute(sql_insert)

    if len(values) > 0:
        sql_insert = assemble_insert(table_name, values)
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
CREATE TABLE "{table_name}" (
    id varchar(255) primary key,
    image varchar(255),
    title varchar(255),
    title_cn varchar(255),
    url varchar(255),
    release_date DATE,
    release_region varchar(255),
    mark float,
    mark_date DATE,
    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP 
);
'''
    db.execute(sql_create)


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(dir_path, 'quotesbot.db'))
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


def main(table_name):
    db = create_connection()
    # create_table(db, table_name)  # once
    data = open_json(table_name)
    insert_table(db, table_name, data)
    close_connection(db)


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) != 2:
    #     print('usage: python dbHelper.py tablename')
    # else:
    #     house = args[1]
        main('my-collect')
