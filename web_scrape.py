from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E85224&propertyTypes=&maxDaysSinceAdded=1&includeLetAgreed=false&mustHave=&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords='
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='propertyCard-wrapper')

results = []

for list in lists:
  address = list.find('address', {'class': 'propertyCard-address', 'itemprop': 'address'})
  address_text = address.find('span').text
  price = list.find('span', class_='propertyCard-priceValue').text
  description = list.find('span',{'itemprop': 'description', 'data-test': 'property-description'}).text
  contact = list.find('a', class_='propertyCard-contactsPhoneNumber').text
  info = [address_text, price,  contact, description]
  if all(info):
    results.append(info)


df = pd.DataFrame(results, columns=['Address', 'Price', 'Contact', 'Description'])
df = df.dropna()
df.to_csv('data.csv')
