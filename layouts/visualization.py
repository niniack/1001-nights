import dash_html_components as html
import dash_core_components as dcc
from layouts.variables import *

# Visualization Layout
layout_visualization = html.Div(
    [
        # Element to output plotly chart
        dcc.Graph(id="output-data", style={"height": "90vh", "width": "90vh"}),
    ],
)
