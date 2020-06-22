import json
import plotly.graph_objects as go

fn = '../data/counties.json'
with open(fn,'r') as fh:
    counties = json.load(fh)

cL = ['salmon','blue']

def poly_for_feature(f):
    vL = f['geometry']['coordinates'][0]
    for t in vL:
        print(t)
    print
    
    X = [t[0] for t in vL]
    Y = [t[1] for t in vL]

    poly = go.Scatter(
        x=X,y=Y,
        line={'color':'black', 'width':3},
        marker={'size':10, 'color':'red'},
        mode='lines+markers',
        fill='toself', 
        fillcolor='blue')
        
    return poly

fig = go.Figure()

fL = [f for f in counties['features'] if f['id'].startswith('01')]

for f in fL:
    p = poly_for_feature(f)
    fig.add_trace(p)
    
fig.update_layout(
    width = 500,
    height = 500,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.2,
    )
)


fig.show()
