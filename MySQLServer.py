import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234' 
        )

        if connection.is_connected():
            cursor = connection.cursor()

            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:

        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
