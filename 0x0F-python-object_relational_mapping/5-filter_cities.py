#!/usr/bin/python3
""" Script that displays all cities belonging to an input state"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    row_count = cur.execute("SELECT name FROM cities WHERE cities.state_id =\
                (SELECT id FROM states WHERE name = %s)", [sys.argv[4]])

    query_rows = cur.fetchall()
    """ Formatted like this to match task format
        And I don't like it """
    for index in range(0, row_count):
        if index < row_count - 1:
            print(query_rows[index][0], end=", ")
        else:
            print(query_rows[index][0], end="")
    print()

    cur.close
    db.close
