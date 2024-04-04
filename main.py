# main.py teste

import mysql.connector
from config import db_config

try:
    # Establishing the connection
    conn = mysql.connector.connect(**db_config)
    
    # Creating a cursor object using the connection
    cursor = conn.cursor()
    
    # Query to execute
    query = "SELECT * FROM your_table_name"
    
    # Executing the query
    cursor.execute(query)
    
    # Fetching all rows from the table
    rows = cursor.fetchall()
    
    # Iterating through rows and printing
    for row in rows:
        print(row)
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
