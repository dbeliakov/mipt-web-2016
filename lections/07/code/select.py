#!/usr/bin/python

import sqlite3


connection = sqlite3.connect("test.db")


def selectAllStudents():
    query = "SELECT users.first_name, users.last_name FROM users WHERE profile = (SELECT id FROM user_types WHERE name = \"Student\");"
    print query
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print row

if __name__ == "__main__":
    selectAllStudents()
