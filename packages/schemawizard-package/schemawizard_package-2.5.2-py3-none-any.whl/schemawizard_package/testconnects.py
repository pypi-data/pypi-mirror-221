"""
  Dave Skura
  
"""
from sqlitedave_package.sqlitedave import sqlite_db

print (" Starting ") # 
db = sqlite_db()
db.connect()
print(db.dbstr())
data = db.query("""SELECT zone,system, ip_address, port, database, version, dba_user, Password
							FROM dbServers
							WHERE upper(database) = upper('MySQL') limit 1""")
for row in data:
	print(row)

db.close()
