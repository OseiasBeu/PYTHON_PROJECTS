import connection
import json
from datetime import datetime

def queryExecute(conn, sql):
	try:
		#conn = connection.getConnection(schema)
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()

	except Exception as e:
	    print(e)

	finally:
	    cursor.close()
	    conn.close()

def queryReturn(conn, sql):

	try:
		#conn = connection.getConnection(schema)
		cursor = conn.cursor()
		cursor.execute(sql)
 	
		rows = cursor.fetchall()

		return rows 

	except Exception as e:
	    print(e)

	finally:
	    cursor.close()
	    conn.close()
