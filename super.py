from flask import Flask, render_template, request
import flask
# from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
import declarations as dc
import json

import os

app = Flask(__name__)

def get_session():
    engine = create_engine('sqlite:///db.sqlite3')
    engine.connect()
    Session = sessionmaker(bind=engine)
    return Session()


@app.route('/super/api/call')
def home():
    session = get_session()
    curr_state = session.query(dc.Current_State).all()[0]
    if curr_state.opened == 1:
        state = session.query(dc.State).filter(dc.State.id == curr_state.id).first()
        votes_yes = session.query(dc.Votes).filter(dc.Votes.state == curr_state.state).filter(
            dc.Votes.vote == 'yes').all()
        votes_no = session.query(dc.Votes).filter(dc.Votes.state == curr_state.state). \
            filter(dc.Votes.vote == 'no').all()

        message = {'command': 'voting', 'payload': 'Votes Yes ' + str(len(votes_yes)) + '   Votes No ' + str(len(votes_no)),
                   'text': state.text}
        return json.dumps(message)
    else:
        message = {'command': 'pass',
                   'payload': ''}
        return json.dumps(message)


static_route = '/super/<path:path>'

@app.route(static_route)
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(
        os.path.join(root_dir, 'static/super'), path
)

# Default port:
if __name__ == '__main__':
    app.run()