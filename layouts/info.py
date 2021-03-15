import dash_html_components as html
import dash_core_components as dcc
from layouts.variables import *

# Visualization Layout
layout_info = dcc.Markdown(
    """
### The Stories and Sub-Stories Within the 1001 Nights


The 1001 Nights are unique because many of the stories within the collection
are frame stories which encompass several other stories. 

The graph on the right is a [Sunburst graph](https://www.fusioncharts.com/resources/chart-primers/sunburst-chart).

Each ring, or level, in the circle represents the layer of sub-story with respect to 
Shahrazad's frame story to King Shahryar. The size of slice in the graph is determined
by the night duration of the story. Moreover, the graph is chronological, with the first story starting at 0&deg;
and moving clockwise.

The idea was inspired by and the data was obtained from [this wonderful blog](https://1001recaps.org/2020/07/06/visualisation/).
The plot was generated using [Plotly and Dash in Python](https://plotly.com/python/sunburst-charts/). The "King of Thieves" font was produced by [Joanna Vu.](https://www.google.com/search?client=ubuntu&hs=cuQ&channel=fs&sxsrf=ALeKk03ndAu3SZrWMlrE2iBeiM889kzb_g%3A1615794543678&ei=bxFPYJH4KIS-tAaAvJDQCQ&q=king+of+thieves+font&oq=king+of+thieves+font&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgIILjICCAAyAggAMgIIADICCC4yAggAMgIIADICCAA6BwgjELADECc6BwguELADEEM6BwgAELADEEM6BAgAEENQtQxY3RFgvxJoAXACeACAAZgCiAGfBpIBAzItM5gBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjR67je57HvAhUEH80KHQAeBJoQ4dUDCAw&uact=5) 

Work done for the [1001 Nights course](https://nyuad.nyu.edu/en/academics/divisions/arts-and-humanities/faculty/paulo-lemos-horta.html ) taught by Professor Paulo Horta. 

Released under the [GNU GPLv3 license.](https://choosealicense.com/licenses/gpl-3.0/)
"""
)
