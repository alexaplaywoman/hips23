# Archivo .py cuya funcion es realizar ajustes previos
# de manera automatica para el funcionamiento del HIPS

import subprocess
import os
import psycopg2
import string
import configparser

# Nombre: crear_dir()
# 
# Esta funcion sirve para crear directorio cuarentena, 
# logs de alarma y de prevencion
#
def crear_dir():
    try:
        #  /tmp/cuarentena almacena carpetas con scripts 
        # sospechos o maliciosos

        if not os.path.exists('/tmp/cuarentena'):
            os.system('sudo mkdir /tmp/cuarentena')
    # cambiamos los permisos
        os.system('chmod 644 /tmp/cuarentena')
    #  /var/logs/hips almacena las alarmas y modulos de prevencion
        if not os.path.exists( '/var/log/hips'):
            os.system('sudo mkdir /var/log/hips')
        os.system('sudo touch /var/log/hips/alarmas.log')
        os.system('sudo touch /var/log/hips/prevencion.log')
    except:
        print("Hubo un error en la creacion de los directorios")

# Nombre: configurar_BD(tp, ts)
#
# Almacena en la base de datos los sha256sum generados
# tp: /etc/password hasheado
# ts: /etc/shadow hasheado
#
def config_BD(tp, ts):
    #buscamos las credenciales
    config = configparser.ConfigParser()
    config.read('secret.ini')
    name_db = config['DEFAULT']['DB_NAME']
    usr_db = config['DEFAULT']['DB_USER']
    pass_db = config['DEFAULT']['DB_PASSWORD']
    #establecemos la conexion
    conn = psycopg2.connect(database=name_db, user=usr_db, password=pass_db)

    #creamos el objeto curso para interactuar con la BD
    curr = conn.cursor()

    #escribimos el query de creacion de BD
    sql = "INSERT INTO sha256sum (file, num_hash) VALUES ('/etc/passwd','" + tp + "'),('/etc/shadow','" + ts + "');"
    #sql = "select * from sha256sum;" 
    print(sql)
    try:
        curr.execute(sql)
        conn.commit()
        print("Carga de datos realizada exitosamente.")
    except psycopg2.Error:
        print("ERROR.")

    #cerramos la conexion
    conn.close()

# Nombre: generar_hash()
#
# Esta funcion tiene como objetivo generar el sha256sum de los dir /etc/passwd
# y /etc/shadow para avisar de posibles modificaciones
#
def generar_hash():
    #generamos los sha256sum
    p = subprocess.Popen('sudo sha256sum /etc/passwd', stdout=subprocess.PIPE, shell=True)
    (out, err) = p.communicate()
    tp = out.decode('utf-8')
    #print(tp)
    tp = tp.split(' ')[0]  #ubicacion del numero hash
    p = subprocess.Popen('sudo sha256sum /etc/shadow', stdout=subprocess.PIPE, shell=True)
    (out, err) = p.communicate()
    ts = out.decode('utf-8')
    ts = ts.split(' ')[0]
    #enviamos a la base de datos
    config_BD(tp, ts)

# Funcion principal
def main():
    crear_dir()
    generar_hash()

if '__main__' == __name__:
  main()
