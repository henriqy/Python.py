from selenium.webdriver import Firefox  
from selenium.webdriver.common.by import By 
from wget import download

driver = Firefox()
driver.get('https://www.instagram.com/bbcbrasil/?hl=pt-br')

driver.implicitly_wait(10) 

frases = driver.find_elements(By.CSS_SELECTOR, 'img.xpdipgo ')

for frase in frases:
    print(frase.get_attribute('src'))
