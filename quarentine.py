# Pone en cuarentena lq le pasas
import subprocess
 
def quarentine(route):
    dir_quarentine = '/tmp/quarantine' 
    command = subprocess.run(['mv', route, dir_quarentine])

#cuarentena('/a')