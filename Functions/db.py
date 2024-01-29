from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

uname = config.get('database', 'uname')
passwd = config.get('database', 'passwd')
host = config.get('database', 'host')
dbname = config.get('database', 'dbname')

engine = create_engine(f'postgresql://{uname}:{passwd}@{host}/{dbname}')
Base = declarative_base()

class Flower(Base):
    __tablename__ = 'flowers'
    id = Column(Integer, Sequence('flower_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(1000))
    growing = Column(String(1000))
    usage = Column(String(1000))
    flowering = Column(String(1000))
    winterizing = Column(String(1000))
    notes = Column(String(1000)) 
    users_flowers = relationship("UsersFlowers", back_populates="flower")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    users_flowers = relationship("UsersFlowers", back_populates="user")

    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
    )

class UsersFlowers(Base):
    __tablename__ = 'users_flowers'
    id = Column(Integer, Sequence('users_flowers_id_seq'), primary_key=True)
    flower_id = Column(Integer, ForeignKey('flowers.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    accuracy = Column(Float, nullable=False)
    photo_url = Column(String(100))
    user = relationship("User", back_populates="users_flowers")
    flower = relationship("Flower", back_populates="users_flowers")

Base.metadata.create_all(engine)