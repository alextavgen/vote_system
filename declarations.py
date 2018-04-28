from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
import declarations as dc

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Current_State(Base):
    __tablename__ = 'Current_State'
    id = Column(Integer, primary_key=True)
    state = Column(Integer, nullable=False)
    opened = Column(Integer, nullable=False)

class State(Base):
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    text = Column(String, nullable=False)
    next_yes= Column(Integer, nullable=False)
    next_no = Column(Integer, nullable=False)


class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False)
    state = Column(Integer, nullable=False)
    vote = Column(String, nullable=False)



engine = create_engine('sqlite:///db.sqlite3')
'''
    sqlite:///:memory: (or, sqlite://)
    sqlite:///relative/path/to/file.db
    sqlite:////absolute/path/to/file.db
'''
connection = engine.connect()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def init():
    state = State(id=0, name='Algus', text = 'KAS SA TAHAD TEADA, KUIDAS KÕIK TULEVIKUS LÄHEB?', next_yes =1, next_no=1000 )
    state1 = State(id=1, name='Tehnika (vol 1.)', text = 'Tehniline tulevik (vol 1.)', next_yes = 2, next_no = 3)
    state2 = State(id=2, name='Tehnika (vol 2.)', text = 'Tehniline tulevik (vol 2.)', next_yes = 4, next_no = 3)
    state3 = State(id=3, name='Multikultuur (vol 1.)', text = 'Multikultuurne tulevik (vol. 1)', next_yes = 11, next_no = 12)
    state4 = State(id=4, name='Katastroof', text = 'Katastroof', next_yes = 5, next_no = 5)
    state5 = State(id=5, name='Võlumaailm', text = 'Võlumaailm', next_yes = 6, next_no = 6)
    state6 = State(id=6, name='Multikultuur(vol.1)', text = 'Multikultuurne tulevik (vol.1)', next_yes = 7, next_no = 8)
    state7 = State(id=7, name='Multikultuur(vol.2)', text = 'Multikultuurne tulevik (vol.2)', next_yes = 8, next_no = 8)
    state8 = State(id=8, name='Kosmos', text = 'Kosmiline tulevik', next_yes = 500, next_no = 9)
    state9 = State(id=9, name='Õkoriik', text = 'Öko tulevik', next_yes = 500, next_no = 10)
    state10 = State(id=10, name='Võlumaailma laul', text = 'Võlumaailma laul', next_yes = 500, next_no = 500)

    state11 = State(id=11, name='Multikultuur (vol 2.)', text = 'Multikultuurne tulevik (vol.2)', next_yes = 12, next_no = 13)
    state12 = State(id=12, name='Katastroof', text = 'Katastroof', next_yes = 666, next_no = 17)
    state17 = State(id=17, name='Võlumaailm', text = 'Võlumaailm', next_yes = 18, next_no = 18)
    state18 = State(id=18, name='Õkoriik', text = 'Öko tulevik', next_yes = 500, next_no = 19)
    state19 = State(id=19, name='Kosmos', text = 'Kosmiline tulevik', next_yes = 500, next_no = 20)
    state20 = State(id=20, name='Võlumaailma laul', text = 'Võlumaailma laul', next_yes = 500, next_no = 500)

    state13 = State(id=13, name='Võlumaailm', text = 'Võlumaailm', next_yes = 14, next_no = 14)
    state14 = State(id=14, name='Katastroof', text = 'Katastroof', next_yes = 666, next_no = 15)
    state15 = State(id=15, name='Õkoriik', text = 'Öko tulevik', next_yes = 500, next_no = 16)
    state16 = State(id=16, name='Kosmos', text = 'Kosmiline tulevik', next_yes = 500, next_no = 20)

    state1000 = State(id=1000, name='Lõpp', text = 'ETENDUS ON LÕPPENUD. PILETIRAHA TAGASI EI SAA', next_yes = 0, next_no = 0)
    state666 = State(id=666, name='LÕPP JA VIIMANE EESTLANE', text = 'LÕPP JA VIIMANE EESTLANE', next_yes = 500, next_no = 20)
    state500 = State(id=500, name='LÕPP JA HÜMN', text = 'LÕPP JA HÜMN', next_yes = 1001, next_no = 1001)
    state1001 = State(id=1001, name='KAS SA TAHAD VALIDA KUIDAS SEE KÕIK TULEVIKUS LÄHEB?', text = 'KAS SA TAHAD VALIDA KUIDAS SEE KÕIK TULEVIKUS LÄHEB?', next_yes = 9999, next_no = 9998)

    session.add(state)
    session.add(state1)
    session.add(state2)
    session.add(state3)
    session.add(state4)
    session.add(state5)

    session.add(state6)
    session.add(state7)
    session.add(state8)
    session.add(state9)
    session.add(state10)
    session.add(state11)

    session.add(state12)
    session.add(state13)
    session.add(state14)
    session.add(state15)
    session.add(state16)
    session.add(state17)

    session.add(state18)
    session.add(state19)
    session.add(state20)
    session.add(state666)
    session.add(state500)
    session.add(state1000)

    session.add(state1001)
    session.commit()

#init()
