"""SpaceX Launch Records Dashboard — Plotly Dash (capstone lab, tasks 1-4)."""
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
                        "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Launch Site Drop-down Input Component
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': s, 'value': s} for s in sorted(spacex_df['Launch Site'].unique())],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    # TASK 2: Pie chart showing successful launches
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Slider to select payload range
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 1000)},
                    value=[min_payload, max_payload]),

    # TASK 4: Scatter chart - payload vs launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2 callback
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        filtered = spacex_df[spacex_df['Launch Site'] == entered_site]
        counts = filtered.groupby('class').size().reset_index(name='count')
        counts['class'] = counts['class'].map({0: 'Failure', 1: 'Success'})
        fig = px.pie(counts, values='count', names='class',
                     title=f'Total Success vs Failure Launches for site {entered_site}')
    return fig


# TASK 4 callback
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    mask = spacex_df['Payload Mass (kg)'].between(low, high)
    filtered = spacex_df[mask]
    if entered_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for site {entered_site}'
    else:
        title = 'Correlation between Payload and Success for All Sites'
    fig = px.scatter(filtered, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category', title=title)
    return fig


if __name__ == '__main__':
    app.run(debug=True)
