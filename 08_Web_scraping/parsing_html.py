import bs4, requests


def getAmazonPrice(productUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/41.0.2228.0 Safari/537.36',}
    res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994', headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newer-version > div > div > div.a-fixed-left-grid-col.a-col-right > span:nth-child(3)')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)
