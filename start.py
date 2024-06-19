# ajustes previos
# de manera automatica para el funcionamiento del HIPS

import subprocess
import os
import psycopg2
import string
import configparser



# Nombre: crear_dir()
#
# Parametros: ninguno
#
# Crear los directorios (si es que no existen)de:
# directorio de cuarentena para procesos sopechosos
# directorios para los registros de alarmas y de prevencion
# 
def create_dir():
    quarentine = '/tmp/quarantine'
    logs = '/var/log/hips'
    if not os.path.exists(quarentine):
        os.system('sudo mkdir /tmp/quarantine')
        #Cambiar los permisos
        os.system('chmod 644 /tmp/quarantine')

    if not os.path.exists(logs):
        os.system('sudo mkdir /var/log/hips')
        if not os.path.isfile('/var/log/hips/alarmas.log'):
            os.system('sudo touch /var/log/hips/alarmas.log')

        if not os.path.isfile('/var/log/hips/prevencion.log'):
            os.system('sudo touch /var/log/hips/prevencion.log')

    

# Funcion principal
def main():
    create_dir()
    

if '__main__' == __name__:
  main()