import mysql.connector
from decouple import config
from mysql.connector import errorcode

configurations = {
    "user": config("USER_NAME"),
    "password": config("PASSWORD"),
    "host": config("HOST"),
    "port": config("PORT"),
    "database": config("DATABASE")
}

try:
    con = mysql.connector.connect(**configurations)
    print("Connected to the MySQL server at port", configurations["port"])
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    con.close()

