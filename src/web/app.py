import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import threading
import time
from collections import deque

# Shared data
time_data = deque(maxlen=200)
temp_data = deque(maxlen=200)
setpoint_data = deque(maxlen=200)
control_data = deque(maxlen=200)
current_setpoint = 50

# Flask server
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H2("Thermal Control Dashboard"),
    dcc.Graph(id='live-graph'),
    dcc.Slider(
        id='setpoint-slider',
        min=20,
        max=80,
        step=1,
        value=current_setpoint,
        marks={i: str(i) for i in range(20, 81, 10)},
    ),
    dcc.Interval(id='graph-update', interval=1000, n_intervals=0)
])

# Callback to update setpoint
@app.callback(
    Output('live-graph', 'figure'),
    Input('graph-update', 'n_intervals'),
    Input('setpoint-slider', 'value')
)
def update_graph(n, setpoint):
    global current_setpoint
    current_setpoint = setpoint
    trace1 = go.Scatter(x=list(time_data), y=list(temp_data),
                        name='Temperature', mode='lines+markers')
    trace2 = go.Scatter(x=list(time_data), y=list(setpoint_data),
                        name='Setpoint', mode='lines', line={'dash':'dash'})
    trace3 = go.Scatter(x=list(time_data), y=list(control_data),
                        name='Heater Output (%)', mode='lines')
    return {'data':[trace1, trace2, trace3],
            'layout': go.Layout(title='Real-Time Temperature Control',
                                xaxis=dict(title='Time (s)'),
                                yaxis=dict(title='Value'))}
