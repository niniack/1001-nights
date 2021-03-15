import plotly.graph_objects as go
import pandas as pd
from layouts.variables import *


def build_sunburst():
    df = pd.read_csv("data/arabian_nights_contents.csv")
    print(df.columns)
    fig = go.Figure(
        go.Sunburst(
            ids=df.id,
            labels=df.name,
            parents=df.parent,
            values=df.night_duration,
            domain=dict(column=0),
            sort=False,
            rotation=90,
            maxdepth=3,
            insidetextorientation="radial",
            marker=dict(colorscale=colorscale),
            hovertemplate="<b>%{label} </b> <br> Nights Duration: %{value}<br>",
        )
    )
    fig.update_layout(grid=dict(columns=1, rows=1), margin=dict(t=0, l=0, r=0, b=0))
    fig.update_layout(paper_bgcolor=bg_color)
    return fig