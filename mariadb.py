#!/usr/bin/env python

import os
import mysql.connector as database

username = "hardi"
password = "hardi"
host = "172.17.0.2"
database_name = "workplace"

connection = database.connect(
    user=username,
    password=password,
    host=host,
    database=database_name
)

cursor = connection.cursor()

def add_data(first_name, last_name):
    try:
      statement = "INSERT INTO employees (first_name,last_name) VALUES (%s, %s)"
      data = (first_name, last_name)
      cursor.execute(statement, data)
      connection.commit()
      print("Successfully added entry to database")
    except database.Error as e:
      print(f"Error adding entry to database: {e}")

def get_data(last_name):
    try:
      statement = "SELECT first_name, last_name FROM employees WHERE last_name=%s"
      data = (last_name,)
      cursor.execute(statement, data)
      for (first_name, last_name) in cursor:
        print(f"Successfully retrieved {first_name}, {last_name}")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

add_data("Super", "Man")
get_data("Man")

connection.close()