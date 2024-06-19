# Nombre: kill_process(pid)
# 
# Parametros: str pid Numero de proceso de pid
#
# Mata el proceso identificado por el PID especificado.

import subprocess

def matar_proceso(pid):
    subprocess.run(['kill', '-9', str(pid)], capture_output=True, text=True)
    #print('Se mato al proceso: '+ str(pid))
