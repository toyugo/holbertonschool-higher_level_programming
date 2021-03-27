#!/usr/bin/python3
""" Description module """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    state_name = str(sys.argv[4])
    cursor = db.cursor()
    mysql_cmd = "SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 INNER JOIN states ON\
                 cities.state_id = states.id\
                 WHERE states.name='{}';".format(state_name)
    cursor.execute(mysql_cmd)
    data = cursor.fetchall()
    i = 0
    for i in range(0, len(data)):
        if i == len(data) - 1:
            print(data[i][1])
        else:
            print(data[i][1], end = ',')
