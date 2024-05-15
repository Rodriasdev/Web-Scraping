import requests
from bs4 import BeautifulSoup

page = "https://pypi.org"

def requestToThePage(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    return soup



def captureTags(url):
    soup = requestToThePage(url)

    results = soup.find_all('a')

    labels={

    }

    for a in results:

        if a['href'][:5] != 'https':
            page = requestToThePage(url + a['href'])

            res = page.find_all(["h1", "p"])

            listOfLabels = []

            for label in res:
                listOfLabels.append(label)
            
            labels[url + a['href']] = listOfLabels


        if a['href'][:5] == 'https':
            page = requestToThePage(a['href'])

            res = page.find_all(["h1", "p"])

            listOfLabels = []

            for label in res:
                listOfLabels.append(label)
            
            labels[a['href']] = listOfLabels

    return labels


print(captureTags(page))


