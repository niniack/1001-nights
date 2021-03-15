import dash_html_components as html
from layouts.inputs import layout_inputs
from layouts.visualization import layout_visualization
from layouts.info import layout_info
from layouts.variables import *

# Main Layout (Two columns: Inputs / Chart)
main_layout = html.Div(
    [
        html.Div(
            [
                html.Div([html.H1(title)]),
            ],
            className="row justify-content-center my-5 mr-5",
        ),
        html.Div(
            [
                html.Div([layout_info], className="col-3"),
                html.Div([layout_visualization], className="col-6"),
                html.Div([layout_inputs], className="col-3"),
            ],
            className="row justify-content-center",
        ),
    ],
    className="container-fluid h-100 mx-5",
)
