import mysql.connector
from mysql.connector import errorcode
from config import *

def connect_to_database():
    try:
      mydb = mysql.connector.connect(user=database_user, password=password,
                                     host=server_address,
                                     database=database_name)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    return mydb



def insert_data(mycursor,insert_query):
    mycursor.execute(insert_query)


def create_table(mycursor,create_query):
    mycursor.execute(create_query)


def drop_table(mycursor,create_query):
    mycursor.execute(create_query)