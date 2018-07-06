from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()

# export SQLALCHEMY_DATABASE_URI=mysql+pymysql://ev100:ev100@127.0.0.1:3306/ev100

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)


class Current_State(Base):
    __tablename__ = 'Current_State'
    id = Column(Integer, primary_key=True)
    state = Column(Integer, nullable=False)
    opened = Column(Integer, nullable=False)

class State(Base):
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    text = Column(String(255), nullable=False)
    next_yes = Column(Integer, nullable=False)
    next_no = Column(Integer, nullable=False)
    immediate = Column(Integer, nullable=False)
    sound_file_start = Column(String(50), nullable=False, default='')
    sound_file_end = Column(String(50), nullable=False, default='')
    vote_type = Column(Integer, nullable=False, default=1)
    switched=Column(Integer, nullable=False, defaul=0)


class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255), nullable=False)
    state = Column(Integer, nullable=False)
    vote = Column(String(10), nullable=False)



engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
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
    state = State(id=0, name='START', text ='Начало', next_yes=1, next_no=1, immediate=0, sound_file_start='START_AUD',
                  sound_file_end='', vote_type=0, switched=0)
    state_check = State(id=1, name='SYMBOLS', text='Введите символы, что вы видите на экране.', next_yes=2, next_no=2, immediate=0, vote_type=1, sound_file_start='SYMBOLS_AUD', sound_file_end='')
    state_complexity = State(id=2, name='COMPLEXITY', text='Выберите уровень сложности', next_yes=100,
                        next_no=100, immediate=0, sound_file_start='COMPLEXITY_AUD', sound_file_end='', vote_type=1)

    state100 = State(id=100, name='G1_ITU', text='Информационно - технологическое государство утопия', next_yes=101, next_no=110, immediate=0)
    state101 = State(id=101, name='G1_ITA', text='Информационно - технологическое государство антиутопия', next_yes=102, next_no=110, immediate=0)
    state102 = State(id=102, name='G1_ITK', text='Информационно технологическая катастрофа', next_yes=5000, next_no=5000, immediate=0)



    state110 = State(id=110, name='G_M/N', text='Мультикультурное государство/Национально-языковое государство', next_yes=200, next_no=400, immediate=1)

    state200 = State(id=200, name='G1_MKU', text='Мультикультурное государство утопия', next_yes=201, next_no=205, immediate=0)
    state201 = State(id=201, name='G1_MKA', text='Мультикультурное государство антиутопия', next_yes=202, next_no=206, immediate=0)
    state202 = State(id=202, name='G1_MKK', text='Мультикультурное государство катастрофа', next_yes=500, next_no=500, immediate=0)

    state205 = State(id=205, name='G_K/O', text='Космическо - колониальное государство утопия/ЭКО государство утопия',
                     next_yes=300, next_no=500, immediate=1)

    state206 = State(id=206, name='G_K/O', text='Национально-языковое государство/Космическо - колониальное государство утопия',
                     next_yes=410, next_no=300, immediate=1)


    state310 = State(id=310, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=311, next_no=5310,immediate=0)
    state311 = State(id=311, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5005,
                     next_no=5311, immediate=0)

    state5310 = State(id=5311, name='MOST',
                     text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=580,
                     next_no=580, vote_type=0, immediate=1,
                     sound_file_start='MOST')

    state5311 = State(id=5311, name='MOST',
                     text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=5005,
                     next_no=570, vote_type=0, immediate=1,
                     sound_file_start='MOST')

    state570 = State(id=570, name='G_ORU', text='ЭКО государство утопия', next_yes=5005, next_no=541, immediate=0)

    state5570 = State(id=5570, name='MOST',
                      text='ФИНАЛЬНЫЙ МОСТ Учитывая предыдущий выбор возможен только этот вариант', next_yes=572,
                      next_no=572, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state572 = State(id=572, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5100, next_no=5100, immediate=1, vote_type=0)

    state580 = State(id=580, name='G_ORU', text='ЭКО государство утопия', next_yes=5580, next_no=5570, immediate=0)

    state5580 = State(id=5580, name='MOST',
                      text='ФИНАЛЬНЫЙ МОСТ Учитывая предыдущий выбор возможен только этот вариант', next_yes=5100,
                      next_no=5100, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state410 = State(id=410, name='G_NYU', text='Национально-языковое государство', next_yes=5005, next_no=999,
                     immediate=0)  # left side

    state415 = State(id=415, name='G_K/O',
                     text='Космическо - колониальное государство утопия/ЭКО государство утопия',
                     next_yes=310, next_no=540, immediate=1)


    ##############
    #leftsecondeco 2

    state500 = State(id=500, name='G_ORU', text='ЭКО государство утопия', next_yes=5005, next_no=501, immediate=0)
    state501 = State(id=501, name='G_ORA', text='ЭКО государство антиутопия', next_yes=502, next_no=5501, immediate=0)
    state502 = State(id=502, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5100, next_no=5100, immediate=1, vote_type=0)

    state5501 = State(id=5501, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=320,
                      next_no=320, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state320 = State(id=320, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=5001,
                     next_no=5001, immediate=0, vote_type=0)


###################from205 206 mide

    state300 = State(id=300, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=301, next_no=305, immediate=0)
    state301 = State(id=301, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5001, next_no=305, immediate=0)

    state305 = State(id=305, name='G_ITK', text='ЭКО государство утопия/Национально-языковое государство',
                     next_yes=550, next_no=400, immediate=1)

    state550 = State(id=550, name='G_ORU', text='ЭКО государство утопия', next_yes=5100, next_no=551, immediate=0)
    state551 = State(id=551, name='G_ORA', text='ЭКО государство антиутопия', next_yes=5570, next_no=5551, immediate=0)

    state5551 = State(id=5551, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=451,
                      next_no=451, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state451 = State(id=451, name='G_NYU', text='Национально-языковое государство', next_yes=5100, next_no=5100,
                     immediate=0, vote_type=0)


    state400 = State(id=400, name='G_NYU', text='Национально-языковое государство', next_yes=5000, next_no=5400,immediate=0)

    state5400 = State(id=5400, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=510,
                      next_no=510, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state510 = State(id=510, name='G_ORU', text='ЭКО государство утопия', next_yes=512, next_no=5001, immediate=0)
    state512 = State(id=512, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5100, next_no=5100, immediate=1, vote_type=0)


######205 after

    state540 = State(id=540, name='G_ORU', text='ЭКО государство утопия', next_yes=5100, next_no=541, immediate=0)
    state541 = State(id=541, name='G_ORA', text='ЭКО государство антиутопия', next_yes=542, next_no=545, immediate=0)
    state542 = State(id=542, name='G_ORK', text='ЭКО государство катастрофа', next_yes=5100, next_no=5100, immediate=1, vote_type=0)

    state545 = State(id=545, name='G_K/N',
                    text='Космическо - колониальное государство утопия/Национально-языковое государство',
                    next_yes=340, next_no=400, immediate=1)

    state340 = State(id=340, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=341, next_no=5340,immediate=0)
    state341 = State(id=341, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5001,
                     next_no=5001,immediate=0, vote_type=0)

    state5340 = State(id=5340, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=440,
                      next_no=440, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state440 = State(id=440, name='G_NYU', text='Национально-языковое государство', next_yes=5100, next_no=5100, vote_type=0,
                     immediate=0)


    state450 = State(id=450, name='G_NYU', text='Национально-языковое государство', next_yes=5100, next_no=5450,immediate=0)

    state5450 = State(id=5450, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=330,
                      next_no=330, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state330 = State(id=330, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=341,
                     next_no=5340, immediate=0, vote_type=0)
#############
##RIGHT

    state405 = State(id=405, name='G_M/N', text='Мультикультурное государство/Космическо - колониальное государство утопия',
                     next_yes=210, next_no=350, immediate=1)

    state210 = State(id=210, name='G1_MKU', text='Мультикультурное государство утопия', next_yes=211, next_no=215,
                     immediate=0)
    state211 = State(id=211, name='G1_MKA', text='Мультикультурное государство антиутопия', next_yes=212, next_no=216,
                     immediate=0)
    state212 = State(id=212, name='G1_MKK', text='Мультикультурное государство катастрофа', next_yes=5005, next_no=5005,
                     immediate=0, vote_type=0)

    state215 = State(id=215, name='G_K/O',
                     text='Национально-языковое государство/Космическо - колониальное государство утопия',
                     next_yes=310, next_no=500, immediate=1)

    state216 = State(id=216, name='G_K/O',
                     text='Национально-языковое государство/Космическо - колониальное государство утопия',
                     next_yes=310, next_no=500, immediate=1)


#####SAME AS LEFT 310-500
#############

###RIGHT EDGE

    state350 = State(id=350, name='G_KKU', text='Космическо - колониальное государство утопия', next_yes=351,
                     next_no=355, immediate=0)
    state351 = State(id=351, name='G_KKA', text='Космическо - колониальное государство антиутопия', next_yes=5001,
                     next_no=355, immediate=0)

    state355 = State(id=355, name='G_ITK', text='ЭКО государство утопия/Мультикультурное государство утопия',
                     next_yes=560, next_no=220, immediate=1)


    state560 = State(id=560, name='G_ORU', text='ЭКО государство утопия', next_yes=5100, next_no=541, immediate=0)
    state561 = State(id=561, name='G_ORA', text='ЭКО государство антиутопия', next_yes=5570, next_no=5561, immediate=0)

    state5561 = State(id=5561, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=230,
                      next_no=230, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state230 = State(id=230, name='G1_MKU', text='Мультикультурное государство утопия', next_yes=221, next_no=5220,
                     immediate=1, vote_type=0)

    state220 = State(id=220, name='G1_MKU', text='Мультикультурное государство утопия', next_yes=221, next_no=5220,
                     immediate=0)
    state221 = State(id=221, name='G1_MKA', text='Мультикультурное государство антиутопия', next_yes=222, next_no=5220,
                     immediate=0)
    state222 = State(id=222, name='G1_MKK', text='Мультикультурное государство катастрофа', next_yes=5005, next_no=5005,
                     immediate=0, vote_type=0)

    state5520 = State(id=5520, name='MOST',
                      text='Учитывая предыдущий выбор возможен только этот вариант', next_yes=570,
                      next_no=570, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state570 = State(id=540, name='G_ORU', text='ЭКО государство утопия', next_yes=5001, next_no=572, immediate=0)
    state572 = State(id=541, name='G_ORA', text='ЭКО государство катастрофа', next_yes=5100, next_no=5100, immediate=0, vote_type=0)




##########


    state5000 = State(id=5000, name='MOST', text='ФИНАЛЬНЫЙ МОСТ Учитывая предыдущий выбор возможен только этот вариант', next_yes=5005, next_no=5005, vote_type=0, immediate=1,
                      sound_file_start='MOST')

    state5001 = State(id=5001, name='MOST',
                      text='ФИНАЛЬНЫЙ МОСТ Учитывая предыдущий выбор возможен только этот вариант', next_yes=5100,
                      next_no=5100, vote_type=0, immediate=1,
                      sound_file_start='MOST')
    state5100 = State(id=5100, name='E_UTO',
                      text='EXIT финал утопий', next_yes=5005,
                      next_no=5005, vote_type=0, immediate=1,
                      sound_file_start='E_UTO')

    state5005 = State(id=5005, name='E_HIMN', text='Exit HÜMN', next_yes=5000, next_no=5000, immediate=0)



    session.add(state)
    session.add(state_check)
    session.add(state_complexity)
    session.add(state100)
    session.add(state101)
    session.add(state102)
    session.add(state110)

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

    session.add(state340)

    session.add(state400)
    session.add(state410)
    session.add(state415)
    session.add(state450)

    session.add(state500)
    session.add(state501)
    session.add(state502)

    session.add(state540)
    session.add(state541)
    session.add(state542)
    session.add(state550)
    session.add(state551)

    session.add(state560)

    session.add(state5000)

    session.add(state5310)
    session.add(state5311)
    session.add(state570)
    session.add(state5570)
    session.add(state572)
    session.add(state570)
    session.add(state580)
    session.add(state5580)
    session.add(state5501)
    session.add(state5551)
    session.add(state451)
    session.add(state510)
    session.add(state512)
    session.add(state5400)
    session.add(state545)
    session.add(state341)
    session.add(state5340)
    session.add(state440)
    session.add(state5450)
    session.add(state405)
    session.add(state210)
    session.add(state211)
    session.add(state212)
    session.add(state215)
    session.add(state216)
    session.add(state350)
    session.add(state351)
    session.add(state355)
    session.add(state561)
    session.add(state5561)
    session.add(state220)
    session.add(state221)
    session.add(state222)
    session.add(state230)
    session.add(state5520)

    session.add(state5001)
    session.add(state5005)
    session.add(state5100)




    session.commit()

if __name__ == '__main__':
    init()
#init()
