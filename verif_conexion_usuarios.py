#Usuarios conectados en el host
import subprocess

def users_conected():
    results = subprocess.run("w",capture_output=True, text=True)
    print(results.stdout)
    #return resultado # enviar al email tal vez.

users_conected()