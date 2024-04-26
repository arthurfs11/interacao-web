# Aqui você encontrará algumas dicas úteis sobre selenium, para verificar como utilizar, olhar o arquivo "importacoes"
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

class DicasSelenium:

    def fechar_navegador(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def aguardar_pag_carregar(self):
            self.driver.get("link da pagina")
            self.driver.implicity_wait(2)
            self.wait_loads()

            return self.driver

    def aguardar_elemento_carregar(self,elemento,time=20,throw=True):
        try:
            objeto = WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located((By.XPATH, elemento)))
            return objeto
        except:
            if throw: raise
            return None

    def rolar_final_pagina(self):
        get_position = lambda:self.driver.execute_script("return document.documentElement.scrollTop")

        while True:
            posicao_atual = get_position()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            posicao_futura = get_position()
            if posicao_futura == posicao_atual:
                break
