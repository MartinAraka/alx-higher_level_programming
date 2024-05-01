#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], state = argv[4])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cursor.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))
    cursor.close()
    db.close()
