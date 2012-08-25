# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import MySQLdb
from datetime import datetime

def changeBrasilValueToEnglishValue(str):
    #Remove period and change comma to period
    while str.find(".") != -1:
        i = str.find(".")
        str=str[0:i]+str[i+1:]
    while str.find(",") != -1:
        i = str.find(",")
        str=str[0:i]+"."+str[i+1:]
    str = changeToDatetime(str)
    return str
def changeToDatetime(string):
    if '/' in string:
        date = datetime.strptime(string,"%d/%m/%Y")
        #return "datetime.date("+str(date.day)+","+str(date.month)+","+str(date.year)+")"
        date = date.strftime("%Y-%m-%d")
        return "'"+date+"'"
    else:
        return string
def changeStrangeStringToFamiliar(string):
    strange = ["\xc2\xba","\xc3\xaa","\xc3\xba","\xd0\xba",]
    familiar = ["o","e","u","e"]
    i = 0
    for s in strange:
        while string.find(s) != -1:
            index = string.index(s)
            string = string[:index]+familiar[i]+string[index+len(s):]
        i+=1
    string = Simplificador(string)
    print "\t" + string
    return string

def Simplificador(str):
    old = ["Bola1","Bola2","Bola3","Bola4","Bola5",
           "Bola6","Bola7","Bola8","Bola9","Bola10",
           "Bola11","Bola12","Bola13","Bola14","Bola15",
           "Valor_Rateio_15_Numeros","Valor_Rateio_14_Numeros","Valor_Rateio_13_Numeros","Valor_Rateio_12_Numeros","Valor_Rateio_11_Numeros",
           "Ganhadores_15_Numeros","Ganhadores_14_Numeros","Ganhadores_13_Numeros","Ganhadores_12_Numeros","Ganhadores_11_Numeros",
           "Estimativa_Preimo","Acumulado_15_Numeros", "Data Sorteio","Arrecadacao_Total","Concurso"] 
    
    new = ["b1","b2","b3","b4","b5",
            "b6","b7","b8","b9","b10",
            "b11","b12","b13","b14","b15",
            'rateio15','rateio14','rateio13','rateio12','rateio11',
            'ganhadores15','ganhadores14','ganhadores13','ganhadores12','ganhadores11',
            'estimativa','acumulado15',"data_sorteio","arrecadacao","concurso"]
    i = 0
    for s in old:
        while str.find(s) != -1:
            index = str.index(s)
            str = str[:index]+new[i]+str[index+len(s):]
        i+=1
    return str


def getLotery(name,file_name):
    print "Loteria " + name
    #File management
    try:
        file = open(file_name,"r")
    except:
        "File " + file_name + " not found"
        return
    
    #Parser management
    print "Analizando arquivo pelo BeautifulSoup"
    soup = BeautifulSoup(file)
    table = soup.findAll("table")[0]
    table_lines = table.findAll("tr")
    first_line = table_lines[0]
    cols_title = first_line.findAll("th")
    
    Loteria = []
    titles = []
    HEAD = True
    cont = 1
    total_cont = len(table_lines)
    for tr in table_lines:
        #Get title
        if HEAD:
            print "Pegando titulos das colunas"
            cols_title = tr.findAll("th")
            #Caso nao ha th's
            if len(cols_title) == 0:
                cols_title = tr.findAll("td")
            for th in cols_title:
                font_tag = th.findAll("font")[0]
                title=str(font_tag.contents[0])
                title=changeStrangeStringToFamiliar(title)
                titles.append(title)
                print "\t" + title
                HEAD = False
            continue
        #Get sorteios
        print "Analizando linha: " + str(cont) + " de " + str(total_cont-1)
        cont+=1
        line_content = tr.findAll("td")
        sorteio = []
        n_column = len(line_content)
        for columN in range(0,n_column):
            value = str(line_content[columN].contents[0])
            value = changeBrasilValueToEnglishValue(value)
            if columN == 1:
                sorteio.append((titles[columN],value))
            else: 
                #Just two decimals places
                try:
                    if type(value) == float:
                        value = "%.2f" % float(value)
                except:
                    pass
                sorteio.append((titles[columN],value))
                #sorteio[titles[columN]] = value    
        Loteria.append(sorteio)
    file = open(name,"w")
    file.write(str(Loteria))
    return Loteria

def getListofColumns(loteria):
    lotoCols = []
    colunas = []
    for tupla in loteria[0]:
        colunas.append(tupla[0])
    return colunas


def getListofValues(loteria):
    valores = []
    for sorteio in loteria:
        for coluna in sorteio:
            valores.append(coluna[1])
        valores.append("")
    return valores



def loteriaToSql(loteria):
    sql_base = "INSERT INTO lotofacil $c VALUES $b;"
    sql_list = []
    
    cols = getListofColumns(loteria)
    cols_str = str(cols)
    cols_str = cols_str.replace("[","(")
    cols_str = cols_str.replace("]",")")
    cols_str = cols_str.replace("'","")

    sql_base = sql_base.replace("$c",cols_str)
    
    
    for sorteio in loteria:
        vals = []
        for coluna in sorteio:
            vals.append(coluna[1])
            vals_str = str(vals)

        
        vals_str = vals_str.replace("[","(")
        vals_str = vals_str.replace("]",")")
        vals_str = vals_str.replace("'","")

        sql_end = sql_base.replace("$b",vals_str)

        #print sql_end
        sql_list.append(sql_end)
    return sql_list

def executeQuery(query,cursor):
    #try:
        #print query
    cursor.execute(query)
    answer = cursor.fetchall()
        #print answer
    #except cursor.ProgrammingError:
     #   print "MySQL error: " + str(cursor.ProgrammingError.message)


# names = ["duplacena","federal","lotofacil","lotogol","lotomania","megasena","quina","timemania"]
# files =["./htmls/duplacena","./htmls/federal","./htmls/lotofacil.htm","./htmls/lotogol.htm","./htmls/lotomania.htm","./htmls/megasena.htm","./htmls/quina.htm","./htmls/timemania.htm"] 
names = ["lotofacil"]
files =["./htmls/lotofacil.htm"] 

n_names = len(names)

for i in range(0,n_names):
    lotofacil = getLotery(names[i],files[i])
#Generating SQL query
print "Generating SQL query"
sqls = loteriaToSql(lotofacil)

#Connectando ao BD
print "Connecting to DB..."
connection = MySQLdb.connect('localhost','root','chronos')
connection.select_db('lotomidas')
cursor = connection.cursor()

#Limpa banco de dados
print "Cleaning banco de dados..."
cursor.execute("TRUNCATE TABLE lotofacil")
cursor.execute("commit")

print "Executing queries..."
for sql in sqls:
    executeQuery(sql,cursor)

print "Commiting changes..."
cursor.execute("commit")
connection.store_result()
