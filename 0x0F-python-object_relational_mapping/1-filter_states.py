#!/usr/bin/python3
""" Description module """
import MySQLdb
import sys


if __name__ == "__main__":
    u_n = sys.argv[1]
    p_n = sys.argv[2]
    d_n = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3303, user=u_n, passwd=p_n, db=d_n)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
