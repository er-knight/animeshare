from sqlalchemy import Column, Integer, Float, String

from database import Base


class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    type = Column(String)
    episodes = Column(Integer)
    status = Column(String)
    airing_period = Column(String)
    image_url = Column(String)
    rank = Column(Integer)
    rating = Column(Float)
