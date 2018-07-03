from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


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
    next_yes = Column(Integer, nullable=False)
    next_no = Column(Integer, nullable=False)
    immediate = Column(Integer, nullable=False)


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
def get_session():
    return Session()

def init():
    state = State(id=0, name='Algus', text ='Intro', next_yes=100, next_no=1000, immediate=0)
    state100 = State(id=100, name='G_ITU', text='Информационно - технологическое государство утопия', next_yes=101, next_no=110, immediate=0)
    state101 = State(id=101, name='G_ITA', text='Информационно - технологическое государство антиутопия', next_yes=102, next_no=110, immediate=0)
    state102 = State(id=102, name='G_ITK', text='Информационно технологическая катастрофа', next_yes=500, next_no=500, immediate=0)



    state105 = State(id=110, name='G_M/N', text='Мультикультурное государство/Национально-языковое государство', next_yes=200, next_no=400, immediate=1)

    state200 = State(id=200, name='G_MKU', text='Мультикультурное государство утопия', next_yes=201, next_no=205, immediate=0)
    state201 = State(id=201, name='G_MKA', text='Мультикультурное государство антиутопия', next_yes=202, next_no=206, immediate=0)
    state202 = State(id=202, name='G_MKK', text='Мультикультурное государство катастрофа', next_yes=500, next_no=500, immediate=0)

    state205 = State(id=205, name='G_K/O', text='Космическо - колониальное государство утопия/ЭКО государство утопия',
                     next_yes=300, next_no=500, immediate=1)

    state206 = State(id=206, name='G_K/O', text='Космическо - колониальное государство утопия/Национально-языковое государство',
                     next_yes=410, next_no=300, immediate=1)

    state300 = State(id=300, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=301, next_no=305, immediate=0)
    state301 = State(id=301, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5000, next_no=305, immediate=0)

    state305 = State(id=305, name='G_ITK', text='ЭКО государство утопия/Национально-языковое государство',
                     next_yes=550, next_no=460, immediate=1)

    state550 = State(id=550, name='G_ORU', text='ЭКО государство утопия', next_yes=5000, next_no=551, immediate=0)
    state551 = State(id=551, name='G_ORA', text='ЭКО государство антиутопия', next_yes=552, next_no=505, immediate=0)
    state552 = State(id=552, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5000, next_no=5000, immediate=0)

    state450 = State(id=450, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=5000,immediate=0)

    state460 = State(id=460, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=560,immediate=0)

    state560 = State(id=560, name='G_ORU', text='ЭКО государство утопия', next_yes=5000, next_no=562, immediate=0)
    state552 = State(id=562, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5000, next_no=5000,immediate=0)

    state400 = State(id=400, name='G_NYU', text='Национально-языковое государство', next_yes=999, next_no=999,immediate=0)

    state410 = State(id=410, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=999,immediate=0) #left side
    state415 = State(id=415, name='G_K/O',
                     text='Космическо - колониальное государство утопия/ЭКО государство утопия',
                     next_yes=310, next_no=540, immediate=1)
    state330 = State(id=330, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=331, next_no=530,immediate=0)
    state331 = State(id=331, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5000,
                     next_no=530,immediate=0)
    state530 = State(id=530, name='G_ORU', text='ЭКО государство утопия', next_yes=5000, next_no=532,immediate=0)
    state532 = State(id=532, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5000, next_no=5000,immediate=0)

    state540 = State(id=540, name='G_ORU', text='ЭКО государство утопия', next_yes=5000, next_no=541,immediate=0)
    state541 = State(id=541, name='G_ORA', text='ЭКО государство антиутопия', next_yes=542, next_no=340,immediate=0)
    state542 = State(id=542, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5000, next_no=5000,immediate=0)
    state340 = State(id=340, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=5000,
                     next_no=500,immediate=0)


    state500 = State(id=500, name='G_ORU', text='ЭКО государство утопия', next_yes=5000, next_no=501, immediate=0)
    state501 = State(id=501, name='G_ORA', text='ЭКО государство антиутопия', next_yes=502, next_no=505, immediate=0)
    state502 = State(id=502, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5000, next_no=5000, immediate=0)

    state505 = State(id=505, name='G_K/N', text='Космическо - колониальное государство утопия/Национально-языковое государство',
                     next_yes=310, next_no=400, immediate=1)

    state310 = State(id=310, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=311, next_no=9,immediate=0)
    state311 = State(id=311, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5000,
                     next_no=9, immediate=0)

    state420 = State(id=420, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=5000, immediate=0)

    state430 = State(id=430, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=5000, immediate=0)
    state320 = State(id=320, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=5000, next_no=5000, immediate=0)



    stateDummy = State(id=999, name='DUMMY', text='DUMMY NOT DEFINED', next_yes=999, next_no=999,immediate=0)

    state5000 = State(id=5000, name='E_UTO', text='Exit финал утопий HÜMN', next_yes=5000, next_no=5000, immediate=0)


    session.add(state)
    session.add(state100)
    session.add(state101)
    session.add(state102)
    session.add(state105)

    session.add(state200)
    session.add(state201)
    session.add(state202)
    session.add(state205)
    session.add(state206)

    session.add(state300)
    session.add(state301)
    session.add(state305)
    session.add(state310)
    session.add(state311)
    session.add(state320)
    session.add(state330)
    session.add(state331)
    session.add(state340)

    session.add(state400)
    session.add(state410)
    session.add(state415)
    session.add(state420)
    session.add(state430)
    session.add(state450)
    session.add(state460)

    session.add(state500)
    session.add(state501)
    session.add(state502)
    session.add(state505)
    session.add(state530)
    session.add(state532)
    session.add(state540)
    session.add(state541)
    session.add(state542)
    session.add(state550)
    session.add(state551)
    session.add(state552)
    session.add(state560)

    session.add(state5000)
    session.add(stateDummy)







    session.commit()

if __name__ == '__main__':
    init()
#init()
