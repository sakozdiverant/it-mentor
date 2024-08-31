import psycopg2

try:
    conn = psycopg2.connect(
        dbname="ITM",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print(f"Failed to connect: {e}")
