import json
from ugeo import fips_to_abbrev

fn = 'counties1.json'
fh = open(fn,'r')

obj = json.load(fh)
L = obj['features']
pL = list()

for e in L:
    if e['geometry']['type'] == 'MultiPolygon':
        name = e['properties']['NAME']
        fips = e['id'][:2]
        abbrev = fips_to_abbrev[fips]
        pL.append((abbrev, name))

pL.sort()
for abbrev, name in pL:
    print('%s, %s' % (name, abbrev))


        
'''
...
Bethel, AK
Hoonah-Angoon, AK
Juneau, AK
Kenai Peninsula, AK
Ketchikan Gateway, AK
Kodiak Island, AK
Lake and Peninsula, AK
Nome, AK
Petersburg, AK
Prince of Wales-Hyder, AK
Sitka, AK
Valdez-Cordova, AK
Wrangell, AK
Mobile, AL
Los Angeles, CA
San Francisco, CA
Santa Barbara, CA
Ventura, CA
...
'''