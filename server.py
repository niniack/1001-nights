import dash

external_stylesheets = [
    {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
        "rel": "stylesheet",
    },
    {
        "href": "/static/style.css",
        "rel": "stylesheet",
        "content-type": "text/css",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Stories of the 1001 Nights"