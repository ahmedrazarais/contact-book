# importing mysql connector and database password user from server details.py file

import mysql.connector
from server_connection import Connection


# making a class for database creation and for table creation for holding accountsdetails
# inherits with connection class
class Database_Creation(Connection):
    def __init__(self):
        super().__init__()
        self.database="contact"

    # making amehtod to create dabase name contact
    def create_database(self):
        try:
            self.create_connection()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # mehtod to create table for accounts holdingin contact database
    def create_table_for_accounts(self):
        try:
            self.cursor.execute(f"USE {self.database} ")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            usernames VARCHAR(50),
            password VARCHAR (50),
            security VARCHAR (50)
            )""")
            
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")