#!-*- conding: utf8 -*-
import zipfile
from subprocess import PIPE
import subprocess

#Global variables
check_directory_exists = """if [ -d 'htmls' ];
                            then echo 'exist';
                            else
                            echo 'empty';
                             fi"""


#Executa processo(command) no linux, retorna uma tupla, tupla[0] = saida, tupla[1]= erro.
def execute(command):
    p = subprocess.Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
    stdout,stderr = p.communicate()
    #Retirar /n, normal na saida do comando
    stdout = stdout.split()
    stderr = stderr.split()
    return (stdout,stderr)

#Check if /htmls directory exist
ask_exist = execute(check_directory_exists)[0]
if ask_exist[0] == "empty":    
    #Cria diretorio
    subprocess.call("mkdir htmls",shell=True)

#Lista os arquivos em /zips
ls = execute("ls ./zips")[0]
n_zips = len(ls)

#Zips e uma lista de tuplas, onde tupla[0] e o nome do arquivo e tupla[1] e o arquivo zipado
zips = []

for zip_name in ls:
    zips.append((zip_name,zipfile.ZipFile("./zips/"+zip_name,"r")))

#Dezipa arquivo e renomeia
for tupla in zips:
    htm_name = tupla[0][:-3]+"htm"
    zip = tupla[1]
    for file_name in zip.namelist():
        if (".htm" in file_name) or (".HTM" in file_name):
            pag = zip.read(file_name)
            file = open("./htmls/"+htm_name,"w")
            file.write(pag)
            print htm_name + " extraido com sucesso."


    

