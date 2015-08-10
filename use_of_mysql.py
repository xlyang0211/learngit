import MySQLdb
import json

# Open file to store the data in world/country;
OUT = file('world_country', 'w')
conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'babygift_49139',
        db = 'test.cpp',
        )
cur = conn.cursor()
cur.execute('use world')
result = cur.execute("select * from country where Name = 'China'")
info = cur.fetchmany(result)
for i in info:
    i_json = json.dumps(i)
    OUT.write(i_json+"\n")
OUT.close()
cur.close()
conn.commit()
conn.close()
