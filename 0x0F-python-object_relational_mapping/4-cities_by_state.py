#!/usr/bin/python3
""" Description module """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    mysql_cmd = "SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 INNER JOIN states ON\
                 cities.state_id = states.id;"
    cursor.execute(mysql_cmd)
    data = cursor.fetchall()
    for row in data:
        print(row)
