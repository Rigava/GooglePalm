import sqlite3
connection = sqlite3.connect("dummy.db")

cursor = connection.cursor()
cursor.execute("create table vesselDetails(imo integer, name text, segment integer, fuelClassId integer, scantDraft integer)")
vessel_detail =[(9999999,"dummy1",2000,100,8),
                (9999998,"dummy2",4000,101,9),
                (9999997,"dummy3",6000,102,10),
                (9999996,"dummy4",8000,103,11)
                ]
cursor.executemany("insert into vesselDetails values (?,?,?,?,?)",vessel_detail)

for row in cursor.execute("select * from vesselDetails"):
    print(row)
connection.close()
