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
