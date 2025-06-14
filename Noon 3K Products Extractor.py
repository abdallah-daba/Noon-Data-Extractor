from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import os
import time

search_terms = ["smart watches", "cell phones", "airpods"]
base_path = r"C:\Users\Power Tech\Desktop\noon_scraping_outputs"
os.makedirs(base_path, exist_ok=True)

def noon(search_query):
    product_details = []
    formatted_query = search_query.replace(" ", "%20")
    base_url = f"https://www.noon.com/egypt-en/search/?q={formatted_query}"

    try:
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)

        page = 1
        max_products = 1000  
        while len(product_details) < max_products:
            current_link = f"{base_url}&page={page}"
            browser.get(current_link)

            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.ProductBoxLinkHandler_linkWrapper__b0qZ9'))
            )

            product_list = browser.find_elements(By.CSS_SELECTOR, 'div.ProductBoxLinkHandler_linkWrapper__b0qZ9')

            if not product_list:
                print(f"❌ No products found on page {page}, stopping.")
                break

            for product in product_list:
                if len(product_details) >= max_products:
                    break

                soup = BeautifulSoup(product.get_attribute('outerHTML'), 'html.parser')

                try:
                    name = soup.find('h2').text.strip()
                except:
                    name = "no product found"

                try:
                    price = soup.find('strong').text
                except:
                    price = "no price found"

                try:
                    discount = soup.find('span', {'class': 'PriceDiscount_discount__1ViHb'}).text
                except:
                    discount = "no discount"

                try:
                    rate = soup.find('div', {'class': 'RatingPreviewStar_textCtr__sfsJG'}).text
                    rate = float(rate)
                except:
                    rate = 0.0

                try:
                    link = soup.find('a').get('href')
                    link = f"https://www.noon.com{link}"
                except:
                    link = "no link"

                product_details.append({
                    'product name': name,
                    'price': price,
                    'discount': discount,
                    'rating': rate,
                    'link': link
                })

            print(f"✅ {search_query.upper()} - Page {page} done ({len(product_details)} total)")
            page += 1
            time.sleep(1)

        browser.quit()
        return product_details

    except Exception as e:
        print(f"❌ Error while scraping {search_query} --> {e}")
        return []

def save_to_csv(keyword, products):
    if not products:
        print(f" No products to save for {keyword}")
        return

    sorted_data = sorted(products, key=lambda x: x['rating'], reverse=True)
    file_path = os.path.join(base_path, f"{keyword.replace(' ', '_')}_noon_products.csv")
    keys = sorted_data[0].keys()

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(sorted_data)

    print(f"✅ Saved {len(sorted_data)} products to: {file_path}")

# Run for all search terms
for term in search_terms:
    results = noon(term)
    save_to_csv(term, results)
