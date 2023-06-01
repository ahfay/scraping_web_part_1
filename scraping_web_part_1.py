from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Cek status 
req = requests.get('https://books.toscrape.com/')
print(req.status_code)

req = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find_all('table', 'table table-striped')
for ekstrak in table:
  list_data = ekstrak.find_all('td')

# Mengecek isi list_data
# print(list_data)

# Membuat kolom untuk Dataframe data yang telah didapatkan
kolom = ['UPC', 'Product Type', 'Price (excl. tax)', 'Price (incl. tax)', 'Tax', 'Availability', 'Number of reviews']
hasil = []

# Memasukkan data ke kolom UPC
upc = list_data[0].text
hasil.append(upc)

# Memasukkan data ke kolom Product Type
product_type = list_data[1].text
hasil.append(product_type)

# Memasukkan data ke kolom Price (excl. tax)
price_excl = list_data[2].text
price_excl = float(price_excl.replace('Â£',''))
hasil.append(price_excl)

# Memasukkan data ke kolom Price (incl. tax)
price_incl = list_data[3].text
price_incl = float(price_incl.replace('Â£',''))
hasil.append(price_incl)

# Memasukkan data ke kolom Tax
tax = list_data[4].text
tax = float(tax.replace('Â£',''))
hasil.append(tax)

# Memasukkan data ke kolom Availability
avail = list_data[5].text
avail = int(avail.replace('In stock (','').replace(' available)',''))
hasil.append(avail)

# Memasukkan data ke kolom Number of reviews
reviews = int(list_data[6].text)
hasil.append(reviews)

# Membuat Dataframe
df = pd.DataFrame(np.array([hasil]), columns=kolom)
df