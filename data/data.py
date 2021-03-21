import plotly.graph_objects as go
import pandas as pd
import numpy as np
from layouts.variables import *

df = pd.read_csv("data/final_arabian_nights.csv")
customdata_df = np.stack(
    (df.night_duration, df.gender_dominance, df.gender_ratio), axis=-1
)
df["color"] = np.where(
    df["gender_ratio"].notna(), np.where(df["gender_ratio"] > 0.5, female, male), mint
)


def build_sunburst():
    story_id = ""
    fig = go.Figure(
        go.Sunburst(
            ids=df.id,
            labels=df.name,
            parents=df.parent,
            values=df.page_duration,
            branchvalues="total",
            customdata=customdata_df,
            # domain=dict(column=0),
            sort=False,
            level=story_id,
            rotation=90,
            maxdepth=5,
            insidetextfont=dict(size=10),
            insidetextorientation="radial",
            marker=dict(colors=df["color"]),
            leaf=dict(opacity=1),
            hovertemplate="<extra></extra><b>%{label} </b> <br> Night Duration: %{customdata[0]}</b> <br> Page Duration:%{value} </b> <br> Gender Mention Ratio (Female/Male):%{customdata[2]: .2f}<br>",
        )
    )
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    fig.update_layout(paper_bgcolor=bg_color)
    return fig


def update_sunburst(story, fig):
    story_loc = df.loc[(df["name"] == story)]
    if len(story_loc):
        story_id = str(story_loc["id"].values[0])
        fig.update_traces(level=story_id, selector=dict(type="sunburst"))
        gender_analysed = story_loc["gender_ratio"].notna().values[0]
        if gender_analysed:
            print(story_loc["gender_ratio"].values[0])

    else:
        fig.update_traces(level="", selector=dict(type="sunburst"))
