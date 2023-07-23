import os

import dash


app = dash.Dash(__name__,)

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)