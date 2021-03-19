import plotly.graph_objects as go
import pandas as pd
from layouts.variables import *

df = pd.read_csv("data/arabian_nights_contents.csv")


def build_sunburst():
    story_id = ""
    # story_loc = df.loc[(df["name"] == story)]
    # if len(story_loc):
    #     story_id = str(story_loc["id"].values[0])
    fig = go.Figure(
        go.Sunburst(
            ids=df.id,
            labels=df.name,
            parents=df.parent,
            values=df.night_duration,
            domain=dict(column=0),
            sort=False,
            level=story_id,
            rotation=90,
            maxdepth=4,
            insidetextorientation="radial",
            marker=dict(colorscale=colorscale),
            hovertemplate="<b>%{label} </b> <br> Nights Duration: %{value}<br>",
        )
    )
    fig.update_layout(grid=dict(columns=1, rows=1), margin=dict(t=0, l=0, r=0, b=0))
    fig.update_layout(paper_bgcolor=bg_color)
    return fig


def update_sunburst(story, fig):
    story_loc = df.loc[(df["name"] == story)]
    if len(story_loc):
        story_id = str(story_loc["id"].values[0])
        fig.update_traces(level=story_id, selector=dict(type="sunburst"))
    else:
        fig.update_traces(level="", selector=dict(type="sunburst"))
