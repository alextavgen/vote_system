import dash
from dash.dependencies import Event, Input, Output
import dash_core_components as dcc
import dash_html_components as html
import flask
import os
import uuid
from dash import DashResponse

import plotly.graph_objs as go
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
import declarations as dc

from sqlalchemy.ext.declarative import declarative_base

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

def get_session():
    engine = create_engine('sqlite:///db.sqlite3')
    engine.connect()
    Session = sessionmaker(bind=engine)
    return Session()

def layout(id):
    # Edit this object!
    return html.Div(
                [
                    html.Div(
                        [
                           id

                        ],
                        className='six columns',
                        style={'margin-top': '10'}
                    ),

                ],
                className='row')

# Barebones layout
app.layout = html.Div([
    dcc.Interval(id='refresh', interval=5000),
# Edit this object!
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div([
                                html.Div([], id='start_content', className="container")
                            ], id='content', className="container"),
                            html.Div(id='graph', className="container")

                        ],
                        className='six columns',
                        style={'margin-top': '10'}
                    ),

                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div([], id='open_div', className="container"),
                    html.Div([], id='close_div', className="container"),
                    html.Button('Tuleb', id='yes'),
                    html.Button('Ei Tule', id='no'),
                ],
                className='six columns'
            ),
        ],

        className='ten columns offset-by-one'
    )

])

def get_wait_for_next(curr_state, id):
    return 'Please wait for start voting'


def get_voted_graph(curr_state, id):
    session = get_session()
    votes_yes = session.query(dc.Votes).filter(dc.Votes.state == curr_state.state).filter(
        dc.Votes.vote == 'yes').all()
    votes_no = session.query(dc.Votes).filter(dc.Votes.state == curr_state.state). \
        filter(dc.Votes.vote == 'no').all()

    labels = ['Tuleb', 'Ei tule']
    values = [len(votes_yes), len(votes_no)]
    colors = ['#96D38C', '#E1396C']

    trace = go.Pie(labels=labels, values=values, marker=dict(colors=colors,
                           line=dict(color='#000000', width=2)))

    figure = {
        'data': [trace]
    }

    return dcc.Graph(id='main_graph',
                     figure=figure,
                     config={
                         'displayModeBar': False,
                     })

# Update the `content` div with the `layout` object.
# When you save this file, `debug=True` will re-run
# this script, serving the new layout
@app.callback(
    Output('content', 'children'),
    events=[Event('refresh', 'interval')])
def display_layout():
    session = get_session()
    curr_state = session.query(dc.Current_State).all()[0]
    id = flask.request.cookies.get('watcher_id')

    if curr_state.opened == 1:
        voted = session.query(dc.Votes).filter(dc.Votes.uuid == id).filter(dc.Votes.state == curr_state.state).all()
        if len(voted) == 0:

            state = session.query(dc.State).filter(dc.State.id==curr_state.state).all()[0]

            response = DashResponse(html.Div(layout(state.text)))
        else:
            response = DashResponse(get_voted_graph(curr_state, id))

    else:
        response = DashResponse(html.Div(get_wait_for_next(curr_state, id)))
    if id is None:
        response.set_cookie('watcher_id', str(uuid.uuid4()))
    return response

@app.callback(
    Output('open_div', 'children'),
    [Input('yes', 'n_clicks')])
def open(n_click):
    session = get_session()
    if n_click is not None:
        curr_state = session.query(dc.Current_State).all()[0]
        id = flask.request.cookies.get('watcher_id')

        if curr_state.opened == 1:
            voted = session.query(dc.Votes).filter(dc.Votes.uuid == id).filter(dc.Votes.state == curr_state.state).all()
            if len(voted) == 0:
                vote = dc.Votes(uuid=id, state=curr_state.state, vote='yes')
                session.add(vote)
                session.commit()


@app.callback(
    Output('close_div', 'children'),
    [Input('no', 'n_clicks')])
def close(n_click):
    session = get_session()
    if n_click is not None:
        curr_state = session.query(dc.Current_State).all()[0]
        id = flask.request.cookies.get('watcher_id')

        if curr_state.opened == 1:
            voted = session.query(dc.Votes).filter(dc.Votes.uuid == id).filter(dc.Votes.state == curr_state.state).all()
            if len(voted) == 0:
                vote = dc.Votes(uuid=id, state=curr_state.state, vote='no')
                session.add(vote)
                session.commit()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

static_route = '/static/<path:path>'

@server.route('/vote')
def vote():
    root_dir = os.getcwd()
    return '{["test"]}'


@server.route('/start')
def index():
    resp = flask.make_response(flask.render_template('index.html'))
    #resp.set_cookie('watcher_id', str(uuid.uuid4()))
    return resp

@server.route(static_route)
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(
        os.path.join(root_dir, 'static'), path
)
if __name__ == '__main__':
    app.run_server(threaded=True, port=8080)
