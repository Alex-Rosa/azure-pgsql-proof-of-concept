import psycopg2

# Establishing the connection
try:
    connection = psycopg2.connect(
        database="your_database_name",
        user="your_username",
        password="your_password",
        host="localhost",  # Change if your database is on another server
        port="5432"        # Default PostgreSQL port
    )
    cursor = connection.cursor()
    print("Connected to the database!")

    # Executing a SELECT statement
    select_query = "SELECT * FROM your_table_name;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("SELECT query results:")
    for row in rows:
        print(row)

    # Executing an INSERT statement
    insert_query = """
    INSERT INTO your_table_name (column1, column2)
    VALUES (%s, %s);
    """
    cursor.execute(insert_query, ("value1", "value2"))
    connection.commit()  # Commit the transaction
    print("INSERT statement executed successfully!")

except Exception as error:
    print(f"An error occurred: {error}")

finally:
    # Closing the connection
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed.")

/////////////////////////////////

pip install azure-identity psycopg2-binary

/////////////////////////////////

import psycopg2

try:
    connection = psycopg2.connect(
        database="your_database_name",
        user="your_username@your_server_name",
        password="your_password",
        host="your_server_name.postgres.database.azure.com",
        port="5432",  # Default PostgreSQL port
        sslmode="require"  # Required for Azure
    )
    print("Connected to Azure PostgreSQL!")
    # Rest of your code (SELECT, INSERT, etc.)
except Exception as error:
    print(f"An error occurred: {error}")
finally:
    if connection:
        connection.close()
        print("Connection closed.")

/////////////////////////////////

from azure.identity import DefaultAzureCredential
import psycopg2

# Get a token from Microsoft Entra
try:
    # Use DefaultAzureCredential to get the access token
    credential = DefaultAzureCredential()
    token = credential.get_token("https://ossrdbms-aad.database.windows.net/.default")

    # Create the connection string with the token
    connection = psycopg2.connect(
        database="your_database_name",
        user="your_username@your_server_name",
        password=token.token,  # Use the token as the password
        host="your_server_name.postgres.database.azure.com",
        port="5432",
        sslmode="require"
    )
    print("Connected to Azure PostgreSQL using Microsoft Entra Authentication!")
    # Rest of your code (SELECT, INSERT, etc.)

except Exception as error:
    print(f"An error occurred: {error}")

finally:
    if connection:
        connection.close()
        print("Connection closed.")
