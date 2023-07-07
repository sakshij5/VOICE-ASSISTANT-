import json

if __name__ == '__main__':
    price_data = None
    price = []
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = json.loads(price_data)

        for d in json_price_data:
            price.append({'name': d['name'], 'price': float(d['amazon_price']), 'url': d['amazon_url']})
            price.append({'name': d['name'], 'price': float(d['walmart_price']), 'url': d['walmart_url']})
            price.append({'name': d['name'], 'price': float(d['ebay_price']), 'url': d['ebay_url']})
            minPricedItem = min(price, key=lambda x: x['price'])
            print(minPricedItem)
            print('=================')
            price = []

            for d in json_price_data:
                price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
                price.append({'name': d['name'], 'price': d['walmart_price'], 'url': d['walmart_url']})
                price.append({'name': d['name'], 'price': d['ebay_price'], 'url': d['ebay_url']})
                minPricedItem = min(price, key=lambda x: float(x['price']))
                store_name = ''
                # Pick the store name based on url
                if 'amazon' in minPricedItem['url'].lower():
                    store_name = 'Amazon'
                elif 'walmart' in minPricedItem['url'].lower():
                    store_name = 'Amazon'
                elif 'ebay' in minPricedItem['url'].lower():
                    store_name = 'eBay'
                print('{} is available in cheap price at {}. The price is ${}'.format(minPricedItem['name'], store_name,
                                                                                      minPricedItem['price']))
                price = []
