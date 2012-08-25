# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup

def changeBrasilValueToEnglishValue(str):
    #Remove period and change comma to period
    while str.find(".") != -1:
        i = str.find(".")
        str=str[0:i]+str[i+1:]
    while str.find(",") != -1:
        i = str.find(",")
        str=str[0:i]+"."+str[i+1:]
    return str

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
    return string

def Simplificador(str):
    old = ["Bola1","Bola2","Bola3","Bola4","Bola5",
           "Bola6","Bola7","Bola8","Bola9","Bola10",
           "Bola11","Bola12","Bola13","Bola14","Bola15",
           "Valor_Rateio_15_Numeros","Valor_Rateio_14_Numeros","Valor_Rateio_13_Numeros","Valor_Rateio_12_Numeros","Valor_Rateio_11_Numeros",
           "Ganhadores_15_Numeros","Ganhadores_14_Numeros","Ganhadores_13_Numeros","Ganhadores_12_Numeros","Ganhadores_11_Numeros",
           "Estimativa_Preimo","Acumulado_15_Numeros", "Data Sorteio","Arrecadacao_Total,Concurso"] 
    
    new = ["b1","b2","b3","b4","b5",
            "b6","b7","b8","b9","b10",
            "b11","b12","b13","b14","b15",
            'rateio15','rateio14','rateio13','rateio12','rateio11',
            'ganhadores15','ganhadores14','ganhadores13','ganhadores12','ganhadores11',
            'estimativa','acumulado',"data_sorteio","arrecadacao","concurso"]
    i = 0
    for s in old:
        while str.find(s) != -1:
            index = str.index(s)
            str = str[:index]+new[i]+str[index+len(s):]
        i+=1
    return str


def getLotery(name,file_name):
    print name
    #File management
    try:
        file = open(file_name,"r")
    except:
        "File " + file_name + " not found"
        return
    
    #Parser management
    soup = BeautifulSoup(file)
    table = soup.findAll("table")[0]
    table_lines = table.findAll("tr")
    first_line = table_lines[0]
    cols_title = first_line.findAll("th")
    
    Loteria = []
    titles = []
    i = 0
    for tr in table_lines:
        print k
        #Get title
        if i == 0:
            cols_title = tr.findAll("th")
            #Caso nao ha th's
            if len(cols_title) == 0:
                cols_title = tr.findAll("td")
            for th in cols_title:
                font_tag = th.findAll("font")[0]
                title=str(font_tag.contents[0])
                title=changeStrangeStringToFamiliar(title)
                titles.append(title)
                i+=1
            continue
        #Get sorteios
        print k
        line_content = tr.findAll("td")
        sorteio = {}
        n_column = len(line_content)
        for columN in range(0,n_column):
            value = str(line_content[columN].contents[0])
            if columN == 1:
                sorteio[titles[columN]] = value
            else: 
                value = changeBrasilValueToEnglishValue(value)
                #Just two decimals places
                try:
                    value = "%.2f" % float(value)
                except:
                    pass
                sorteio[titles[columN]] = value    
        Loteria.append(sorteio)
    file = open(name,"w")
    file.write(str(Loteria))

# names = ["duplacena","federal","lotofacil","lotogol","lotomania","megasena","quina","timemania"]
# files =["./htmls/duplacena","./htmls/federal","./htmls/lotofacil.htm","./htmls/lotogol.htm","./htmls/lotomania.htm","./htmls/megasena.htm","./htmls/quina.htm","./htmls/timemania.htm"] 
names = ["lotofacil"]
files =["./htmls/lotofacil.htm"] 

n_names = len(names)
for i in range(0,n_names):
    getLotery(names[i],files[i])

