from server import app
from layouts.main import main_layout
from data.data import build_sunburst

# Include layout
app.layout = main_layout

# Include callbacks (Needs to be assigned after setting layout up)
from callbacks.main import *

server = app.server
fig = build_sunburst()

# Initializing app
if __name__ == "__main__":
    app.run_server(debug=True)
