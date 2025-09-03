import json
import re
import time
import uuid

from get_conn import GetConn
from datetime import datetime
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

PATH_DRIVER = r"C:\Users\yastr\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'books_to_scrape'
}


service = Service(PATH_DRIVER)
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")  # não abre janela
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=chrome_options)
@dataclass
class Book():
    upc: str
    title: str
    category: str
    img_link: str
    description: str
    star_rating: int
    br_price: float
    stock_quantity: int

rating_text_to_int = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

BOOK_ERRORS = []

def scrape_books(links):
    books_to_insert = []
    for link in links:
        try:
            driver.get(link)

            upc = driver.find_element(By.XPATH,"//table//tr[th[text()='UPC']]/td").text
            title = driver.find_element(By.CLASS_NAME, "product_main").find_element(By.TAG_NAME, "h1").text
            img_link = driver.find_element(By.CSS_SELECTOR,"div.col-sm-6:not(.product_main) img").get_attribute("src")

            le_price = driver.find_element(By.CLASS_NAME, "price_color").text
            br_price = float(le_price.replace("£", "")) * 7.31
            
            star_rating_class = driver.find_element(By.CLASS_NAME, "star-rating").get_attribute('class')
            star_rating = rating_text_to_int[star_rating_class.split()[1]]
            
            stock_text = driver.find_element(By.CLASS_NAME, "instock").text
            stock_quantity = int(re.search(r"\((\d+) available\)", stock_text).group(1))
            try:
                description = driver.find_element(By.CSS_SELECTOR, "#product_description + p").text
            except Exception:
                description = None
                
            breadcrumb_items = driver.find_elements(By.CSS_SELECTOR, "ul.breadcrumb li a")
            if len(breadcrumb_items) >= 2:
                category = breadcrumb_items[-1].text

            book_id = str(uuid.uuid4())
            created_at = updated_at = datetime.now()

            books_to_insert.append((
                book_id, upc, title, category, img_link,
                description, star_rating, br_price,
                stock_quantity, created_at, updated_at
            ))
        except Exception as e:
            BOOK_ERRORS.append({'link': link, 'error': str(e)})
            continue
    return books_to_insert

        
def insert_books(db_config, books_to_insert):
    with GetConn(db_config) as db:
        # Checar duplicidade e filtrar
        books_final = []
        books_to_update = []
        for book in books_to_insert:
            upc = book[1]
            category = book[3]

            db.cursor.execute("SELECT id, category FROM books WHERE upc = %s", (upc,))
            result = db.cursor.fetchone()

            if result:
                book_id, existing_category = result
                if not existing_category and category:
                    books_to_update.append((category, book_id))
            else:
                books_final.append(book)

        if books_final:
            sql = """
                INSERT INTO books (
                    id, upc, title, category, img_link, description,
                    star_rating, br_price, stock_quantity,
                    created_at, updated_at
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            db.cursor.executemany(sql, books_final)
            db.conn.commit()
            print(f"{len(books_final)} livros inseridos")
        else:
            print("Nenhum livro novo para inserir")

        if books_to_update:
            sql_update = """UPDATE books SET category = %s, updated_at = NOW() WHERE id = %s"""
            db.cursor.executemany(sql_update, books_to_update)
            db.conn.commit()
            print(f"{len(books_to_update)} livros inseridos")



# https://www.receiteria.com.br/
# https://www.themealdb.com/browse/area/ca
page_link = "https://books.toscrape.com"
time.sleep(2)

books_to_insert = []
try:
    while True:
        driver.get(page_link)
        image_container = driver.find_elements(By.CLASS_NAME, "image_container")
        links = [c.find_element(By.TAG_NAME, "a").get_attribute('href') for c in image_container]
        books_to_insert.extend(scrape_books(links))
        
        if len(links) < 20:
            BOOK_ERRORS.append({'page': page_link, 'links': links})
        
        driver.get(page_link)
        
        if len(books_to_insert) >= 80:
            insert_books(db_config, books_to_insert)
            books_to_insert = []
            time.sleep(5)
        
        try:
            page_link = driver.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME, 'a').get_attribute('href')
        except NoSuchElementException:
            print("Não há botão 'next', fim das páginas")
            break
except Exception as e:
    print(f'Error: {e}')
finally:
    driver.quit()
    
insert_books(db_config, books_to_insert)

with open("book_errors.json", "w", encoding="utf-8") as f:
    json.dump(BOOK_ERRORS, f, ensure_ascii=False, indent=4)