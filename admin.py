import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, Event, State
import declarations as dc
import plotly.graph_objs as go

app = dash.Dash()
app.layout =html.Div(
        [
            dcc.Interval(id='refresh', interval=5000),
            html.Div(
                [
                    html.Div(
                        [
                            html.P('Press button:'),
                            html.Button('Start voting', id='start', className='button-primary'),
                        ],
                        className='twelve columns'
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div([
                                html.Div([], id='start_content', className="container")
                            ], id='content', className="container")

                        ],
                        className='twelve columns',
                        style={'margin-top': '10'}
                    ),
                    html.Div(
                        [

                        ],
                        className='twelve columns',
                        id = 'graph',
                        style={'margin-top': '10'}
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div([], id='open_div', className="container"),
                    html.Div([], id='close_div', className="container"),
                    html.Button('Open voting', id='open', className='button-primary four columns'),
                    html.Div([], className='four columns'),
                    html.Button('Close voting', id='close', className='button-primary four columns'),
                ],
                className='twelve columns'
            ),
        ],

        className='ten columns offset-by-one'
    )

@app.callback(
    Output('graph', 'children'),
    events=[Event('refresh', 'interval')])
def votes_show():
    curr_state = dc.session.query(dc.Current_State).all()[0]
    if curr_state.opened == 1:
        votes_yes = dc.session.query(dc.Votes).filter(dc.Votes.state == curr_state.state).filter(
            dc.Votes.vote == 'yes').all()
        votes_no = dc.session.query(dc.Votes).filter(dc.Votes.state == curr_state.state). \
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
    else:
        return None

def wrap_state(state):
    if not state:
        return None
    return html.Div([state[0].text])

@app.callback(
    Output('start_content', 'children'),
    [Input('start', 'n_clicks')])
def start(n_click):
    if n_click is not None:
        dc.session.query(dc.Current_State).delete()
        dc.session.query(dc.Votes).delete()
        dc.session.commit()
        curr_state = dc.Current_State(id=0, state=0, opened=0)
        dc.session.add(curr_state)
        dc.session.commit()
        state = dc.session.query(dc.State).filter(dc.State.id==0).all()
        return wrap_state(state)

@app.callback(
    Output('open_div', 'children'),
    [Input('open', 'n_clicks')])
def open(n_click):
    if n_click is not None:
        state = dc.session.query(dc.Current_State).filter().all()
        new_state = state[0]
        new_state.opened = 1
        dc.session.add(new_state)
        dc.session.commit()

@app.callback(
    Output('close_div', 'children'),
    [Input('close', 'n_clicks')])
def close(n_click):
    if n_click is not None:
        curr_state = dc.session.query(dc.Current_State).all()[0]
        if curr_state.opened == 1:
            votes_yes = dc.session.query(dc.Votes).filter(dc.Votes.state == curr_state.state).filter(
                dc.Votes.vote == 'yes').all()
            votes_no = dc.session.query(dc.Votes).filter(dc.Votes.state == curr_state.state). \
                filter(dc.Votes.vote == 'no').all()

            if dc.session.query(dc.State).filter(dc.State.id == curr_state.state).all():
                state = dc.session.query(dc.State).filter(dc.State.id == curr_state.state).all()[0]

                if len(votes_yes) >= len(votes_no):
                    next_state_id = state.next_yes
                else:
                    next_state_id = state.next_no

                dc.session.query(dc.Current_State).delete()
                dc.session.commit()
                next_state = dc.session.query(dc.State).filter(dc.State.id == next_state_id).first()
                if next_state.immediate == 0:
                    curr_state = dc.Current_State(state=next_state_id, opened=0)
                else:
                    curr_state = dc.Current_State(state=next_state_id, opened=1)
                dc.session.add(curr_state)
                dc.session.commit()

                state_next = dc.session.query(dc.State).filter(dc.State.id==next_state_id).all()[0]

                return 'Выбрано ' + state_next.text
            else:
                return None

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
