from dataclasses import dataclass
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




PATH_DRIVER = r"C:\Users\yastr\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(PATH_DRIVER)

# options = Options()
# options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=service,
    # options=options
)

@dataclass
class Book():
    title: str
    description: str
    br_price: float
    availability: bool
    stock_qtd: int
    star_rating: int
    


try:
    # Abrir o site
    driver.get("https://books.toscrape.com")
    time.sleep(2)  # espera a página carregar
    
    books_elements = driver.find_elements(By.CLASS_NAME, "product_pod")
    
    links = []
    for book_element in books_elements:
        link = book_element.find_element(By.CLASS_NAME, "image_container").find_element(By.TAG_NAME, "a").get_attribute('href')
        links.append(link)
    
    for link in links:
        
        driver.get(link)
        

    print(f'Quantidade de links: {len(links)}')
    print(links)
    
    

finally:
    driver.quit()