from selenium.webdriver import Firefox  
from selenium.webdriver.common.by import By 
from wget import download
driver = Firefox()
driver.get('https://www.pensador.com/bom_dia_mensagens_e_frases/')

frases = driver.find_elements(By.CSS_SELECTOR, 'div.callout p')

for frase in frases:
    print(frase.text)
    
imagens = driver.find_elements(By.CSS_SELECTOR, 'div.content-img img')

for img in imagens:
    imagem_link = (img.get_attribute('src'))
    download(imagem_link)
