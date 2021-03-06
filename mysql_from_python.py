import os
import pymysql

# Get username from Gitpod workspace

username = os.getenv('Gitpod_User')

# Connect to the Database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whther above was successful or not
    connection.close()
