from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Trailer(Base):
    __tablename__ = 'trailers'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, unique=True)
    title = Column(String)
    poster_url = Column(String)
    synopsis = Column(String)
    cast = Column(String)
    trailer_url = Column(String)

engine = create_engine('sqlite:///trailers.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
