# Pone en cuarentena la ruta del directorio con posible scripts maliciosos
import subprocess
 
def cuarentena(ruta):
    ruta_cuarentena = '/cuarentena' 
    comando = subprocess.run(['mv', ruta, ruta_cuarentena])

