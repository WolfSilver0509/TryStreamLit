import streamlit as st
import pandas as pd
import numpy as np
import unidecode

st.title('My first app')

# ----------------------------------------------------------------------
# Import des librairies
import requests
from bs4 import BeautifulSoup as bs
url_page_produit = ' http://books.toscrape.com/catalogue/sharp-objects_997/index.html'




# On crée une reponse qui va recuperer l'url si tout est ok (200 )
response = requests.get(url_page_produit)
soup = bs(response.text, 'lxml')

if response.ok:
    product_page_url = url_page_produit
    table = soup.findAll('td')
    title = soup.find('h1').text
    universal_product_code = table[0].text
    price_including_tax = table[2].text.replace('£', '£').replace('Â', '')
    price_excluding_tax = table[3].text.replace('£', '£').replace('Â', '')
    number_available = table[5].text.removeprefix('In stock (').removesuffix('available)')
    product_description_unicode = soup.select_one('article > p').text
    product_description = unidecode.unidecode(product_description_unicode)
    category = soup.find('ul', class_="breadcrumb").findAll('a')[2].text
    review_rating = soup.find('p', class_='star-rating').get('class').pop()
    image = soup.find('div', class_="item active").find('img')

    book = {"product_page_url": product_page_url,
            "title": title,
            "product_description": product_description,
            "universal_product_code": universal_product_code,
            "price_including_tax": price_including_tax,
            "price_excluding_tax": price_excluding_tax,
            "category": category,
            "review_rating": review_rating,
            "image": image,
            "number_available": number_available}




st.write("🎯 Le lien de la page du livre est :", product_page_url)
st.write("📕 Le titre du livre est :", title)
st.write("📖 La déscription du livre est :", product_description)
st.write("🔎 Le code Universel de produit :", universal_product_code)
st.write("💰 Le prix en incluant les taxes :", price_including_tax)
st.write("💸 Le prix en excluant les taxes :", price_excluding_tax)
st.write("💸 La catégories du livre est :", category)
st.write("📊 La note du livre :", review_rating, " ⭐")
st.write("📷 L'image du livre ' :", image),
st.write("📷 Le stock disponible du livre :", number_available)




