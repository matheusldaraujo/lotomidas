import subprocess
lotogol="http://www1.caixa.gov.br/loterias/_arquivos/loterias/d_lotogo.zip"
megasena="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip"
quina="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip"
timemania="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_timema.zip"
lotomania="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip"
duplasena="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip"
federal="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_federa.zip"
lotofacil="http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
dict_download = {"lotogol":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/d_lotogo.zip",
                  "megasena":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip",
                  "quina":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip",
                  "timemania":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_timema.zip",
                  "lotomania":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip",
                  "duplasena":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip",
                  "federal":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_federa.zip",
                  "lotofacil":"http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"}

subprocess.call("mkdir zips ",shell=True)
for game in dict_download.iteritems():   
    #Download
    subprocess.call("wget " + game[1],shell=True)
    filename = game[1][game[1].rfind("/")+1:]
    print filename
    #Rename
    subprocess.call("mv "+filename+" ./zips/"+game[0]+".zip",shell=True)
    