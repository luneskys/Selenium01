from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar o navegador Edge
navegador = webdriver.Edge()

# Abrir o site de relações com investidores da Magazine Luiza
navegador.get("https://ri.magazineluiza.com.br/")

# Clicar no link da imagem
navegador.find_element(By.XPATH, '/html/body/form/div[12]/div/div/div[1]/div/div[4]/div/a/img').click()

# Clicar no elemento com o XPath especificado
navegador.find_element(By.XPATH, '//*[@id="D6OClzrGtocpQRELDA4Klw=="]').click()