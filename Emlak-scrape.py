import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


#Define URL (Book)

url="https://emlak.az/"

# Request page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


# Prepare excel
wb = Workbook()
ws = wb.active
ws.title = "Emlak Scrape"
ws.append(["Price", "Attributes"])


# Scrape listing
emlak=soup.find_all("div", class_="ticket-item")


for product in emlak:
    
    price_tag = product.find("div", class_="price-ticket")
    attribute_tag = product.find("div", class_="description-ticket")


    price=price_tag.get_text(strip=True) if price_tag else ""
    attribute=attribute_tag.get_text(strip=True) if attribute_tag else ""
    

    if price and attribute:
        ws.append([price, attribute, ])

    # Save Excel
wb.save("Emlak.xlsx")
print("Done: emlak-scrape.xlsx")

    


