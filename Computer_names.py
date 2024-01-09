import requests
from bs4 import BeautifulSoup
def clean_price(price):
    return int(price.replace(',', '').replace('.', '').split()[0][:-2])
def extract_names_and_prices(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    computers = soup.find_all('section', class_='product_single__wrapper_category')
    for computer in computers:
        print("Computer found")
        name_element = computer.find('a', class_='product_single__product_name_link')
        price_element = computer.find('span', class_='product_single__price_content-discount')
        if name_element and price_element:
            name = name_element.text
            price = clean_price(price_element.text)
            print(f"Computer Name: {name}")
            print(f"Product Price: {price} RSD\n")
if __name__ == "__main__":
    url_page = "https://www.monitor.rs/pc-brand?limit=12&sort=artid_desc&strana=0&price_retail=Min:6155-Max:1438485&stock=Raspolo%C5%BEivo&"
    extract_names_and_prices(url_page)
