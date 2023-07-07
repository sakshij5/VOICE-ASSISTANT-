import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
search = input()
fl_url = "https://www.flipkart.com/search?q="+search
amz_url = "https://www.amazon.in/s?k="+search
product =[]
prices =[]
ratings =[]
fl = requests.get(fl_url).text
amz = requests.get(amz_url).text
soupfl = BeautifulSoup(fl, 'lxml')
soupamz = BeautifulSoup(amz, 'lxml')
#product = soup.find('div')
#print(product.text)
#print(soup.prettify())
productfl = soupfl.find('div', class_= '_4rR01T')
price = soupfl.find('div', class_='_30jeq3 _1_WHN1')
print(productfl.text)
print(price.text)
productamz = soupamz.find('span', class_= 'a-size-medium a-color-base a-text-normal')
print(productamz.text)
