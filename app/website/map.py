import plotly.graph_objects as go
import pandas as pd

from plotly.offline import plot


def generate_plot_div():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

    fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorscale = 'Reds',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix = '$',
        colorbar_title = 'GDP<br>Billions US$',
    ))

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='',
            showarrow = False
        )],
        margin=dict(
            l=10,
            r=10,
            b=10,
            t=10,
            pad=1
        ),
    )
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div