import requests
from bs4 import BeautifulSoup

response = requests.get("https://pypi.org")

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('a')

for a in results:
    print(a)