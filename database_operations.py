# database_operations.py

import mysql.connector
from config import db_config, query_template
from datetime import datetime

def connect():
    """Establishes a connection to the database and returns the connection object."""
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None

def fetch_all_rows(table_name):
    """Fetches all rows from a specified table and prints the operation's timing information."""
    conn = connect()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Start time
            start_time = datetime.now()

            # Prepare query using the template
            query = query_template.format(table_name=table_name)
            cursor.execute(query)
            rows = cursor.fetchall()

            # Finish time
            finish_time = datetime.now()

            # Calculate duration
            duration = (finish_time - start_time).total_seconds()

            # Print timing information
            print(f"Query start time: {start_time}")
            print(f"Query finish time: {finish_time}")
            print(f"Query duration: {duration} seconds")

            return rows
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            if cursor:
                cursor.close()
            conn.close()
