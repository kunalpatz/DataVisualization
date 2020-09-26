"""
        *Data Visualization*
DASH: A simple data visualization tool

* DataSet Used:
    Japan earthquakes 2001 - 2018

* Authors:
    PATIL Kunal (Artificial Intelligence Systems)
    MARATH-PONMADOM (Data Science and Analytics)

"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

file = "Japan earthquakes 2001 - 2018.csv"
data = pd.read_csv(file)

fig_scatter_mapbox = px.scatter_mapbox(data, lat="latitude", lon="longitude", color="mag", size_max=15, zoom=5,
                                       mapbox_style="stamen-terrain")

fig_line = px.line(data, x="time", y="mag")

fig_density_contour = px.density_contour(data, x="time", y="mag")

fig_scatter = px.scatter(data, x="place", y="time",
                         color="mag", hover_name="mag")

app.layout = html.Div(children=[
    html.H1(children='Welcome to a DataViz Project using DASH', style={'color': 'blue', 'fontSize': 48}),
    html.H3(children='Created by: Kunal PATIL (AIS) and Salil MARATH-PONMADOM (DSA)',
            style={'color': 'grey', 'fontSize': 20}),

    html.Div(children='''
        Magnitude of Earthquakes in Japan during 2001-2018 
    '''),
    dcc.Graph(
        id='JE1',
        figure=fig_scatter_mapbox,
    ),
    html.H6(
        children="Observation and Comments: Using Scatter Mapbox, We can observe geaographical distribution of Earthquake's origin."
                 "All the earthquakes originated from east side in pacific ocean. The count is highest during year 2011-12",
        style={'color': 'black', 'fontSize': 12}),
    dcc.Graph(
        id='JE2',
        figure=fig_line
    ),
    html.H6(
        children="Observation and Comments: As observed from scatter mapbox, we know the count is highest during 2011-12. "
                 "With Line graph, we can see the highest magnitude of earthquake observed in March 2011 (9.1)",
        style={'color': 'black', 'fontSize': 12}),
    dcc.Graph(
        id='JE3',
        figure=fig_density_contour
    ),
    html.H6(
        children="Observation and Comments: With Density Contour Maps, "
                 "we can see the highest distribution of earthquakes was observed on July 2, 2011 with count 705 and average magnitude 4.6",
        style={'color': 'black', 'fontSize': 12}),
    dcc.Graph(
        id='JE4',
        figure=fig_scatter
    ),
html.H6(
        children="Observation and Comments: With Scatter, we can observe that earthquakes are more constant on place \"Izu Island\" over the decade"
                 "and There are constant earthquakes obsereved on all places since 2012 till 2018 with average maginitude of 4.9",
        style={'color': 'black', 'fontSize': 12})
])

if __name__ == '__main__':
    app.run_server(debug=True)
