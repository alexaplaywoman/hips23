import psycopg2

def create_db():
    # Establish global connection to the default database
    conn = psycopg2.connect(database="postgres", 
                            user="postgres", 
                            host="localhost",
                            password="123457",
                            port=5432)

    # Enable autocommit (optional but recommended)
    conn.autocommit = True
    # Open a cursor within the global connection
    cur = conn.cursor()

    try:
        # Execute DROP DATABASE outside a transaction
        cur.execute("DROP DATABASE IF EXISTS hips_data;")

        # Execute CREATE DATABASE outside a transaction
        cur.execute("CREATE DATABASE hips_data;")
        print("Database has been created successfully !!")
    finally:
        # Close the cursor (but keep the connection open)
        cur.close()

    # Close the connection to the default database
    conn.close()

def create_tables():
    # Establish global connection to the default database
    conn = psycopg2.connect(database="hips_data", 
                            user="postgres", 
                            host="localhost",
                            password="123457",
                            port=5432)

    # Enable autocommit (optional but recommended)
    conn.autocommit = True
    # Open a cursor within the global connection
    cur = conn.cursor()
    cur.execute("""CREATE TABLE hash(
            id  SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            hash_value VARCHAR(255) NOT NULL
            );""")
        # Make the changes to the database persistent
    conn.commit()

    print("Table has been created successfully !!")
    # Close cursor and communication with the database
    cur.close()
    conn.close()

create_db()
create_tables()