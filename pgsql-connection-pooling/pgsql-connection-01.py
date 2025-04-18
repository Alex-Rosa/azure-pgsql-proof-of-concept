import psycopg2
import time

# Establishing the connection
try:
    connection = psycopg2.connect(
        database="covetrus_01",
        user="postgres",
        password="257672MyLabs1234",
        host="pgsql-01-v16-257672.postgres.database.azure.com",  # Change if your database is on another server
        port="5432"        # Default PostgreSQL port
    )
    cursor = connection.cursor()
    print("Connected to the database!")

    # Executing a SELECT statement
    select_query = "SELECT * FROM public.session_status;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("SELECT query results:")
    for row in rows:
        print(row)

    # Executing an INSERT statement
    #insert_query = """
    #INSERT INTO your_table_name (column1, column2)
    #VALUES (%s, %s);
    #"""
    #cursor.execute(insert_query, ("value1", "value2"))
    #connection.commit()  # Commit the transaction
    #print("INSERT statement executed successfully!")

    # Simulate some delay to observe connection status
    print("-----------------------Sleeping for 600 seconds-----------------------")
    time.sleep(600)

except Exception as error:
    print(f"An error occurred: {error}")

finally:
    # Closing the connection
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed.")

