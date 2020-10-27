from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_bailiff_auctions_text():
    return '''create table if not exists bailiff_auctions_text(
                id int not null primary key,
                category varchar(255) null,
                auction_text varchar(20000) not null,
                timestamp timestamp default CURRENT_TIMESTAMP not null 
                on update CURRENT_TIMESTAMP)'''

def create_bailiff_auctions_fields():
    return'''create table if not exists bailiff_auctions_fields(
                id int not null primary key,
                category varchar(255) null,
                address varchar(255) null,
                estimated_sum varchar(255) null,
                starting_price varchar(255) null,
                auction_date varchar(255) null,
                latitude varchar(255) null,
                longitude varchar(255) null,
                link varchar(255) null,
                timestamp timestamp default CURRENT_TIMESTAMP not null 
                on update CURRENT_TIMESTAMP,
                is_active tinyint(1) default 1 null)'''


class Bailiff_auctions_text(Base):
    __tablename__ = 'bailiff_auctions_text'
    id = Column(Integer,primary_key=True)
    children = relationship("bailiff_auctions_fields")

class Bailiff_auctions_fields(Base):
    __tablename__ = 'bailiff_auctions_fields'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('bailiff_auctions_text.id'))