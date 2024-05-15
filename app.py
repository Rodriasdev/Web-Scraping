import requests
from bs4 import BeautifulSoup

response = requests.get("https://pypi.org")

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('a')

for a in results:

    if a['href'][:5] != 'https':
        info = requests.get(f"https://pypi.org{a['href']}")

        print(info)
    else:
        info = requests.get(a['href'])

        print(info)