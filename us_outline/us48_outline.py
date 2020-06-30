import sys, json

home = '/Users/telliott'
base = home + '/Dropbox/Github/maps'
sys.path.insert(0, base + '/data_geo')

from ugeo import fips_to_abbrev as D
D[''] = ''

fn = 'gz_2010_us_outline_20m.json'
fh = open('../data_geo/src' + '/' + fn,'r')

obj = json.load(fh)
fL = obj['features']

# nothing but LineStrings
for e in fL:
    kind = e['properties']['TYPE']
    right = e['properties']['R_STATEFP']
    left = e['properties']['L_STATEFP']
    
    r = D[right]
    l = D[left]
    if r in ['AK','HI','PR']:
        continue
    
    print(','.join([kind,r,l]))

    cL = e['geometry']['coordinates']
    for long,lat in cL:
        print('%.10f, %.10f' % (long,lat))
    print('')


 