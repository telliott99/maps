import plotly.graph_objects as go

fn = 'counties.geo.txt'
with open(fn) as fh:
    data = fh.read().strip().split('\n\n')

D = {}
L = [e for e in data if 'Alabama' in e]

for e in L:
    vL = list()
    title, rest = e.strip().split('\n',1)
    fips = title.strip().split()[0]
    rest = rest.strip().split('\n')
    X = []
    Y = []
    for line in rest:
        lon, lat = line.strip().split('\t')
        X.append(lon)
        Y.append(lat)
    D[fips] = {'X':X, 'Y':Y}


fig = go.Figure()

for fips in D:
    v = D[fips]
    poly = go.Scatter(
        x=v['X'],y=v['Y'],
        line={'color':'black', 'width':3},
        #marker={'size':10, 'color':'red'},
        #mode='lines+markers',
        mode='lines',
        fill='toself', 
        fillcolor='salmon',
        showlegend=False)
    fig.add_trace(poly)

fig.update_layout(
    width = 1000,
    height = 1000,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.0,
    )
)

fig.show()
