import sqlite3


def drop_all_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table_name in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]};")
        print(f"Dropped table {table_name[0]}")

    conn.commit()
    conn.close()


drop_all_tables('mydatabase.db')
