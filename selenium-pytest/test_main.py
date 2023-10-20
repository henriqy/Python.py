#Realizar imports necessarios

import pytest # Importaçao da biblioteca que iremos trabalhar
from selenium import webdriver 
from selenium.webdriver.common.by import By # usado para localizar elementos na página da web, como botões, campos de texto, links, etc.
import time # permite controlar o tempo de espera em nosso código.

# Configuracoes para abertura do Browser

@pytest.fixture # fornece um recurso ou configuração para os testes. Neste caso, a fixture irá configurar o navegador antes dos testes.
def browser():
    driver = webdriver.Chrome()  # iniciando um navegador e armezanando sua instancia
    yield driver
    driver.quit()  # Fecha o navegador após o teste

# Teste de Adicionar ao Carrinho
def test_addToCart(browser):
		
    product = "Sauce Labs Backpack"
    browser.get("https://www.saucedemo.com/")
   
    usernameInput = browser.find_element(By.NAME, "user-name")  # Use o método By.NAME
    passwordInput = browser.find_element(By.XPATH, '//*[@id="password"]') # Use o método By.Xpath
    loginButton = browser.find_element(By.ID, 'login-button')
    usernameInput.send_keys("standard_user")
    passwordInput.send_keys("secret_sauce") 
    loginButton.click()    

    backpack = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    backpack.click()

    addToCartButton = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    cartButton = browser.find_element(By.CLASS_NAME, "shopping_cart_link")

    addToCartButton.click()
    cartButton.click()

    titleProductInCart = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')

    assert product in titleProductInCart.text