# import json to sqlite db

from sqlite3 import Error
from helper import db_helper
from . import *


def main():
    db = db_helper.create_connection()

    with open('create_tables.sql') as sqls:
        commands = str.split(sqls.read(), ';')

    for c in commands:
        try:
            db.execute(c)
        except Error as e:
            print("[ERROR]", e)

    db.commit()
    db_helper.close_connection(db)

    insert_movie_detail_api.main()
    insert_movie_detail_ranking_api.main()
    insert_movie_detail_credits_api.main()
    insert_my_collect_api.main()


if __name__ == '__main__':
    main()
