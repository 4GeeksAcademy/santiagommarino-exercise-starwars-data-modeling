import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable = False)
    firstname = Column(String(50), nullable = False) 
    lastname = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False)
    password = Column(String(20), nullable = False)

    posts = relationship('Post', back_populates = 'user')
    comments = relationship('Comment', back_populates = 'user')
    followers = relationship('Follower', foreign_keys='Follower.user_to_id', back_populates='user_to')
    following = relationship('Follower', foreign_keys='Follower.user_from_id', back_populates='user_from')

class Follower(Base):
    __tablename__ = 'follower'

    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    user_from = relationship('User', foreign_keys=[user_from_id], back_populates='following')
    user_to = relationship('User', foreign_keys=[user_to_id], back_populates='followers')

class Characters(Base):
    __tablename__ = 'characters'

    id= Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    gender=Column(String(250))
    height=Column(String(250))
    hair_color=Column(String(250))
    eye_color=Column(String(250))
    birth_year=Column(Integer)

class Planets(Base):
    __tablename__= 'planets'

    id=Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    climate= Column(String(250))
    population= Column(Integer)
    diameter= Column(Float)
    terrain = Column(String)
    surface_water= Column(Integer)
    orbital_period= Column(Integer)

class Vehicles(Base):
    __tablename__= 'vehicles'

    id= Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    model_name= Column(String(250))
    manufacturer= Column(String(250))
    price= Column(Integer)

class Favorites(Base):
    __tablename__= 'favorites'

    id= Column(Integer, primary_key=True) 
    user_id= Column(Integer, ForeignKey('user.id'))
    characters_id= Column(Integer, ForeignKey('characters.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))
    vehicles_id= Column(Integer, ForeignKey('vehicles.id'))

class Post(Base):
    __tablename__= 'post'

    id= Column(Integer, primary_key=True) 
    description= Column(Text)
    body= Column(Text)
    user_id= Column(Integer, ForeignKey('user.id'))


    user= relationship('User', back_populates='posts')
    comment= relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
