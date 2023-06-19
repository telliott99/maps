import sys, os
base = os.getenv('covid_base')
sys.path.insert(0,base)

import myutil.ustates as ustates

p = '../../data/states_admitted.txt'
with open(p) as fh:
    data = fh.read()
    
L = data.strip().split('\n')
L = [e for e in L if not e == '']

#-------------------

sL = []
yL = []

def filter(y):
    if y < 1791:  return 0
    if y < 1804:  return 1
    if y < 1822:  return 2
    if y < 1851:  return 3
    if y < 1877:  return 4
    if y < 1891:  return 5
    if y < 1913:  return 6
    return 7

for e in L:
    state,date = e.strip().split(',')
    year = int(date.strip().split('-')[0])
    sL.append(state)
    yL.append(filter(year))

sL = [ustates.state_to_abbrev[state] for state in sL]

#--------------------

import plotly.express as px

cL = ['white','black'] * 4

fig = px.choropleth(
    locations = sL,
    locationmode="USA-states",
    color=yL,
    color_discrete_sequence=cL, 
    scope="usa")

# print(fig)

fig.show()
