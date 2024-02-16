import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=phones+under+15000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&as-pos=1&as-type=RECENT&suggestionId=phones+under+15000%7CMobiles&requestId=09629f91-671e-46f2-a693-2a5412446747&as-searchtext=phones%20under%2015000"

r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
print(soup)