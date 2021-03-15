import numpy as np
from server import app
from dash.dependencies import Input, Output
from data.data import build_sunburst


@app.callback(
    Output("output-data", component_property="figure"),
    [
        Input("input-stdv", "value"),
    ],
)
def update_visualization(dummy):
    # Generates a plotly chart
    sunburst = build_sunburst()
    return sunburst
