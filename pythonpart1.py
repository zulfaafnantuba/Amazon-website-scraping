import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_product_listings(base_url, num_pages=20):
    product_data = []

    for page_num in range(1, num_pages + 1):
        page_url = f"{base_url}&page={page_num}"
        response = requests.get(page_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', class_='s-result-item')

            for product in products:
                product_link = product.find('a', class_='a-link-normal')
                if product_link:  # Check if a valid link element was found
                    product_url = product_link['href']

                    product_name_element = product.find('span', class_='a-text-normal')
                    if product_name_element:  # Check if a valid name element was found
                        product_name = product_name_element.text
                    else:
                        product_name = "N/A"

                    product_price_element = product.find('span', class_='a-price-whole')
                    if product_price_element:  # Check if a valid price element was found
                        product_price = product_price_element.text
                    else:
                        product_price = "N/A"

                    rating = product.find('span', class_='a-icon-alt')
                    num_reviews = product.find('span', class_='a-size-base')

                    if rating:
                        rating = rating.text
                    else:
                        rating = "N/A"

                    if num_reviews:
                        num_reviews = num_reviews.text
                    else:
                        num_reviews = "N/A"

                    product_data.append({
                        'Product URL': product_url,
                        'Product Name': product_name,
                        'Product Price': product_price,
                        'Rating': rating,
                        'Number of Reviews': num_reviews
                    })

    return product_data

amazon_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
num_pages_to_scrape = 20

product_listings = scrape_amazon_product_listings(amazon_url, num_pages_to_scrape)

df = pd.DataFrame(product_listings)

df.to_csv('amazon_product_listings.csv', index=False)
