# python3 extract_counties.py > counties.geo.txt
import sys, os, json

base = os.environ.get('covid_base')
sys.path.insert(0,base)

from myutil.ustrings import abbrev_to_state, territories_to_abbrev
from myutil.ugeo import fips_to_abbrev

# GeoJSON data for US counties

fn = base + '/data_geo/counties.json'
with open(fn,'r') as fh:
    counties = json.load(fh)
    
#---------------------------------

L = counties['features']
for f in L:

    # some are nested 2-deep
    # [[ [lon,lat], 
    # but some are nested 3-deep, such as Bethel, AK
    # [[[ [lon,lat],
    
    vL = f['geometry']['coordinates'][0]
    if (type(vL[0][0])) != type(3.14):
        vL = vL[0]
    
    fips = f['id']
    county = f['properties']['NAME']
    abbrev = fips_to_abbrev[fips[:2]]
    if abbrev in territories_to_abbrev.values():
        continue
    
    state = abbrev_to_state[abbrev]

    print(fips, county, state)
    for t in vL:
        t = (str(e) for e in t)
        print('\t'.join(t))
    print()