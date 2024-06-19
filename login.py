import psycopg2
import hashlib
from .salt_pepper import create_secure_password


# Conexión a la base de datos PostgreSQL
db = psycopg2.connect(
  host="localhost",
  user="postgres",
  password="postgres"
)

cursor = db.cursor()


def create_user(username, password):
  
  # Genera un hash seguro
  password_hash = create_secure_password(password)  
  
  # Dividir hash
  salt, key = password_hash[:16], password_hash[16:]
  hash_algo = "PBKDF2"
  iterations = 100_000

  # Insertar en la base de datos
  insert_sql = (
     "INSERT INTO accounts (username, password_hash, salt, "
     "hash_algo, iterations) "
     "VALUES (%s, %s, %s, %s, %s);"
  )

  cursor.execute(insert_sql, (
     username,
     key,
     salt,
     hash_algo,
     iterations
  ))

  db.commit()


def login(username, password):
  # Obtener detalles del hash de la base de datos
  select_sql = "SELECT * FROM accounts WHERE username = %s"
  
  cursor.execute(select_sql, (username,))
  account = cursor.fetchone()
  
  if not account:
    print("Nombre de usuario inválido")
    return
  
  salt, key, hash_algo, iterations = account[2:6]
  
  # Recalcular el hash con la contraseña ingresada por el usuario
  password_hash = hashlib.pbkdf2_hmac(
    hash_algo,
    password.encode('utf-8'),
    salt,
    iterations
  )
  
  # Comparar los hashes
  if password_hash == key:
    print("Inicio de sesión exitoso")
  else:
    print("Contraseña inválida")
