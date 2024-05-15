import requests
from bs4 import BeautifulSoup

url = "https://pypi.org"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('a')


labels={

}

for a in results:

    if a['href'][:5] != 'https':
        page = requests.get(url + a['href'])
        
        changeformat = BeautifulSoup(page.text, 'html.parser')

        res = changeformat.find_all(["h1", "p"])

        dicOfLabels = []

        for label in res:
            dicOfLabels.append(label)
        
        labels[url + a['href']] = dicOfLabels

    else:
        page = requests.get(a['href'])

        changeformat = BeautifulSoup(page.text, 'html.parser')

        res = changeformat.find_all(["h1", "p"])

        dicOfLabels = []

        for label in res:
            dicOfLabels.append(label)
        
        labels[a['href']] = dicOfLabels

print(labels)