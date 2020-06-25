# python3 extract_counties.py > counties2.geo.txt

# got GeoJSON counties from another source to check
# invalid utf-8 for '72045' Comer_o, Puerto Rico
# Puerto Rico municipios

# found the site of the error by loading binary and 
# searching on the index of the error


import sys, os, json
from operator import itemgetter

base = os.environ.get('covid_base')
sys.path.insert(0,base)

from myutil.ustrings import abbrev_to_state, territories_to_abbrev
from myutil.ugeo import fips_to_abbrev

# GeoJSON data for US counties

fn = sys.argv[1]

try:
    fh = open(fn,'r')
    counties = json.load(fh)
    
except UnicodeDecodeError:
    fh = open(fn,'rb')
    s = fh.read()
    data = s.decode('ISO-8859-1')
    tmp = open('.tmp','w')
    tmp.write(data)
    fh = open('.tmp','r')
    counties = json.load(fh)
    
#---------------------------------

L = counties['features']
pL = []

for f in L:
    try:
        fips = f['id']
    except KeyError:
        fips = f['properties']['GEO_ID'][-5:]
    county = f['properties']['NAME']
    abbrev = fips_to_abbrev[fips[:2]]
    
    if abbrev in territories_to_abbrev.values():
        continue
    
    state = abbrev_to_state[abbrev]
    cL = f['geometry']['coordinates']
    
    # this is wrong
    sL = cL[0]
    pL.append((fips, county, state, sL))
    
pL.sort(key=itemgetter(2,1))
    
for fips, county, state, vL in pL:
    print('\n'.join([county,state,fips]))

    for t in vL:
        t = (str(e) for e in t)
        print('\t'.join(t))
    
    print('')