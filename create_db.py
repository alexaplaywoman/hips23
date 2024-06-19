import psycopg2

conn = psycopg2.connect(database = "hips_data", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgresql",
                        port = 5432)


# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE accounts(
            id  SERIAL PRIMARY KEY,
            username VARCHAR (50) UNIQUE NOT NULL,
            password_hash VARCHAR (500) NOT NULL,
            salt VARCHAR(100) NOT NULL),
            hash_algo VARCHAR(10),
            iterations INT;
            """)
# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()