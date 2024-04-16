import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        user = 'root',
        password = 'Fireboy2.0',
        host = '127.0.0.1',
        database = 'dpd-project')
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database: ", err)
   
else:
    connection.close()


