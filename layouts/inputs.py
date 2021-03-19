import dash_html_components as html
import dash_core_components as dcc
from layouts.variables import *
from data.data import df
from collections import OrderedDict

# Convert HTML directory to python list

names = df["name"].values
directory = [{"label": n, "value": n} for n in names]

# Input layouts
layout_inputs = html.Div(
    [
        html.H3(input_title),
        # Average
        html.Div(
            children=[
                html.Label("Look for a story to expand"),
                dcc.Dropdown(
                    id="story",
                    options=directory,
                    placeholder="Select a story",
                    optionHeight=50,
                    style={"color": "black", "height": "100%"},
                ),
            ],
        ),
    ],
    style={"width": "60%", "height": "100%"},
)


# layout_inputs = html.Div(
#     [
#         html.H3(input_title),
#         html.Div(
#             children=[
#                 # Average
#                 html.Div(
#                     children=[
#                         html.Label("Mean"),
#                         dcc.Input(
#                             id="input-mean",
#                             type="number",
#                             className="form-control",
#                             value=0,
#                         ),
#                     ]
#                 ),
#             ],
#             className="row",
#         ),
#         html.Div(
#             children=[
#                 # Standard Deviation
#                 html.Div(
#                     children=[
#                         html.Label("Standard Deviation"),
#                         dcc.Input(
#                             id="input-stdv",
#                             type="number",
#                             className="form-control",
#                             value=1,
#                         ),
#                     ]
#                 ),
#             ],
#             className="row",
#         ),
#     ]
# )
