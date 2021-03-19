import numpy as np
from server import app
from dash.dependencies import Input, Output
from data.data import build_sunburst, update_sunburst
from app import fig


@app.callback(
    Output("output-data", component_property="figure"),
    [
        Input("story", "value"),
    ],
)
def update_visualization(story):
    update_sunburst(story, fig)
    return fig
