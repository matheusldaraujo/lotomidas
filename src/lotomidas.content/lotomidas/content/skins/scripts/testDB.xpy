import sqlalchemy
import subprocess
from subprocess import PIPE
def script():
    engine = sqlalchemy.create_engine('mysql://root:chronos@localhost/loteria?charset=utf8&use_unicode=0', pool_recycle=3600)
    connection = engine.connect()   
    result = connection.execute("show tables")
    import ipdb;ipdb.set_trace()

def writeFile():
	file = open("casa1", "w")
	file.write("Casa")

def openFile():
	file = open("casa1","r")
	return file.read()

def execute(command):
    p = subprocess.Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
    stdout,stderr = p.communicate()
    #Retirar /n, normal na saida do comando
    stdout = stdout.split()
    stderr = stderr.split()
    return (stdout,stderr)



writeFile()
return openFile()
return execute("'ls'")[0]
