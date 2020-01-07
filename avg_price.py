# IMPORTANT!!! url must be in double quotes
# example: python avg_price.py "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone+x+256+verizon&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"

import sys
import requests
from lxml import html

def search_item(item_url):
    total = 0
    num_phones = 0
    mean = 0
    bn2 = []
    r = requests.get(item_url)
    tree = html.fromstring(r.content)
    phone_prices = []
    phone_prices = tree.xpath("//span[@class='POSITIVE']/text()")
    #print(phone_prices) # Prints array of unpared phone prices.
    for x in phone_prices:
        y = x.replace('$', '')
        temp = y.split('.')
        y = temp[0]
        if (len(y) > 3):
            y = y.replace(',', '')
        int_y = int(y)
        bn2.append(int_y)
        num_phones += 1

    for i in bn2:
        try:
            total += i
        except:
            print("Total integer too large at index: " + i)
    try:
        mean = total / num_phones
    except:
        print "Mean could not be calculated."

    # Print to used number of phones used to arrive at the mean.
    print("Total number of items averaged: " + str(num_phones))
    return mean

url = sys.argv[1]
avg_price = search_item(url)
print "eBay's average price: ", avg_price
