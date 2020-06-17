import pymysql
# Function return a connection.
def getConnection(host, username, password, banco):

	# Connect to the database
	conn = pymysql.connect(
		host = host,
	    user = username,
		password = password,
		db = banco,
	    cursorclass = pymysql.cursors.DictCursor #retorna consulta com titulo
	    )

	return conn
