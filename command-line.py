import sys
import json
import mysql.connector
from mysql.connector import errorcode

def connectDatabase(config):
    try:
        connection = mysql.connector.connect(
            user=config['user'],
            password=config['password'],
            host=config['host'],
            database=config['database']
        )

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Invalid credentials')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database not found')
        else:
            print('Cannot conect to database:', err)
        
    else:
        print("Connected to Database")
        connection.close()

if __name__ == "__main__":
    configFileLocation = sys.argv[1]
    configFile = open(configFileLocation)
    configFileJSON = json.load(configFile)
    connectDatabase(configFileJSON)

# run command: python3 command-line.py config.json