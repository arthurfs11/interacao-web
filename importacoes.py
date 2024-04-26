#aqui você aprende a usar métodos de outros arquivos
from dicas import * # aqui importamos tudo que está no arquivo "dicas"

def fluxo_trabalho(): #aqui criamos o fluxo de trabalho principal 
    selenium = DicasSelenium() #aqui importamos a classe de dicas dentro da variável local #selenium

    #STEP 1
    selenium.aguardar_elemento_carregar() #aqui chamamos a função aguardar_elemento_carregar da classe DicasSelenium (ref. como selenium)

    #STEP 2 
    selenium.rolar_final_pagina()
