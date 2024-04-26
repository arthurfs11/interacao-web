#este template irá contemplar interação web, para isso iremos utilizar o selenium
from selenium import webdriver #webdriver é o módulo para interagir com o navegador
from selenium.webdriver.common.by import By #o módulo By é utilizado para interagir com elementos
from selenium.webdriver.common.keys import Keys #keys são utilizados para enviar comandos de teclado
import time #time é utilizado para conseguirmos utilizar parametrizações de tempo no projeto

driver = webdriver.Chrome() #aqui estamos setando o chrome como navegador

url_site = "aqui você coloca a url do site que vai acessar" #a variável url_site carrega o link do site que o robô deverá acessar

#PASSO 1 - ABRIR O SITE 
driver.get(url_site) #aqui o bot abre o site
time.sleep(5) #colocamos uma pausa de 5 segundos para aguardar o site carregar
#driver.open_page(url_site) #aqui podemos usar apenas este comando, pois o open_page por si só aguarda até o carregamento

#PASSO 2 - INTERAGINDO COM OBJETOS
''' Para interagir com objetos, temos um pequeno caminho a percorrer:
    1. Imagine que você quer clicar no botão de login do facebook, para isso você deverá:
        1.1 Clicar com o botão direito na página e clicar em "Inspecionar"
        1.2 usar o botão "inspecionar elemento" (no MacOS, é command + control + c) e clicar sobre o botão da página que você quer interagir
        1.3 clicar com o botão direito sobre o elemento e clicar em "copy full xpath"
'''
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click() #aqui estamos falando que ele vai buscar o elemento pelo xpath, e ao encontrá-lo, irá clicar sobre ele.
#Nota: o comando "find_element" busca apenas um elemento, já o "find_elements" buscará todos os elementos com o xpath informado e retorna tudo em uma variável de lista
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("aqui você digita o que o robô tem que escrever")# o conceito de utilizar type box é o mesmo, copiar o xpath, e ao invés de colocar "click" usamos o "send_keys" (enviar teclas/simular digitação)
 
#PASSO 3 - CAPTURAR INFORMAÇÕES 
driver.find_element(By.XPATH, "Aqui você coloca o elemento").get_attribute("Aqui você coloca o atributo que você quer")

#PASSO 4 - FECHAR O NAVEGADOR
driver.quit()
