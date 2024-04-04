from database_operations import fetch_all_rows

def main():
    table_name = 'your_table_name'  # replace with your table name
    rows = fetch_all_rows(table_name)
    
    if rows is not None:
        for row in rows:
            print(row)

if __name__ == "__main__":
    main()
