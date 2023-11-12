import os
import mysql.connector
from mysql.connector import errorcode

while True:
  # print("Attempting to connect with " \
  #       f"USER: {os.environ.get('USER')} "\
  #       f"PASSWORD: {os.environ.get('PASSWORD')} "\
  #       f"DATABASE: {os.environ.get('DATABASE')}")

  try:
      cnx = mysql.connector.connect(
          user=os.environ.get('USER', 'keycloak'),
          password=os.environ.get('PASSWORD', 'keycloak'),
          host=os.environ.get('HOST', '127.0.0.1'),
          database=os.environ.get('DATABASE', 'keycloak')
      )
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    print("Connection successful")
    cnx.close()