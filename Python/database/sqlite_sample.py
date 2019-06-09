#!/usr/bin/env python3

import sqlite3 as lite
import sys


DB_PATH = "test_sqlite.db"


def main():
    check_version()
    create_table()
    get_data()


def check_version():
    con = None
    try:
        con = lite.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("SELECT SQLITE_VERSION()")
        row_version = cur.fetchone()
        print("SQLite version:", row_version)
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def create_table():
    con = None
    try:
        con = lite.connect(DB_PATH)
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Languages(Id INT, Name TEXT)")
            cur.execute("INSERT INTO Languages VALUES(1,'Python')")
            cur.execute("INSERT INTO Languages VALUES(2,'Java')")
            cur.execute("INSERT INTO Languages VALUES(3,'SQL')")
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def get_data():
    con = None
    try:
        con = lite.connect(DB_PATH)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Languages")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    main()
