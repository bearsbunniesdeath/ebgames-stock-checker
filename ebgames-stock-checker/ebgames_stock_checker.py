import requests
import argparse

API_ENDPOINT = 'https://www.ebgames.ca/StoreLocator/GetStoresForStoreLocatorByProduct/'

def print_stock(id, city):
    r = requests.get(API_ENDPOINT, params={'value': id, 'skuType': 1, 'language': 'en-CA'})
    r.raise_for_status()

    stores = r.json()
    
    storesInCity = [store for store in stores if store['City'] == city]
    
    if len(storesInCity) > 0:      
        print('Stock availability for %i in %s'%(id, city))
        print('\n'.join('{}: {}'.format(s['Name'], s['ProductStatus']) for s in storesInCity))
    else:
        print('No stores found for %s.'%(city))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='EBGames stock checker')
    parser.add_argument('ids', metavar='ID', type=int, nargs='+', help='a product ID')
    parser.add_argument('--city', default='Calgary', type=str, dest='city')

    args = parser.parse_args()

    for id in args.ids:
        print_stock(id, args.city)

    
