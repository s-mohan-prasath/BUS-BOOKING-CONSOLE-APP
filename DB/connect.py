import mysql.connector as connector
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')
DB = os.getenv('DB')


def connectToDB():
    connection = None
    try:
        connection = connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB
        )
    except connector.Error as e:
        print("Error ---> ", e)
    print("Connected to database")
    return connection


def check_table_exists(c, table_name):
    cursor = c.cursor()
    query = f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def create_table(c, query):
    cursor = c.cursor()

    query = f"CREATE TABLE {query}"

    cursor.execute(query)


def insert_auth_data(c, username, passcode):
    cursor = c.cursor()

    query = f"INSERT INTO User (username,passcode) VALUES ({username},{passcode})"

    cursor.execute(query)
