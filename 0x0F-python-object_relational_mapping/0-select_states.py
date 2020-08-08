#!/usr/bin/python3
""" Script that gets all states from a database, ordered by id """

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close
    db.close
