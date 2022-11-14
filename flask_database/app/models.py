import datetime as dt
from flask import current_app as app
#from app import db
db = app.extensions['sqlalchemy'].db

from werkzeug.security import generate_password_hash, check_password_hash


from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, text, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)    
    
class Country(Base):
    __tablename__ = 'country'

    Code = Column(CHAR(3), primary_key=True, server_default=text("''"))
    Name = Column(CHAR(52), nullable=False, server_default=text("''"))
    Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'), nullable=False, server_default=text("'Asia'"))
    Region = Column(CHAR(26), nullable=False, server_default=text("''"))
    SurfaceArea = Column(DECIMAL(10, 2), nullable=False, server_default=text("0.00"))
    IndepYear = Column(SMALLINT(6))
    Population = Column(INTEGER(11), nullable=False, server_default=text("0"))
    LifeExpectancy = Column(DECIMAL(3, 1))
    GNP = Column(DECIMAL(10, 2))
    GNPOld = Column(DECIMAL(10, 2))
    LocalName = Column(CHAR(45), nullable=False, server_default=text("''"))
    GovernmentForm = Column(CHAR(45), nullable=False, server_default=text("''"))
    HeadOfState = Column(CHAR(60))
    Capital = Column(INTEGER(11))
    Code2 = Column(CHAR(2), nullable=False, server_default=text("''"))

class City(Base):
    __tablename__ = 'city'

    ID = Column(INTEGER(11), primary_key=True)
    Name = Column(CHAR(35), nullable=False, server_default=text("''"))
    CountryCode = Column(ForeignKey('country.Code'), nullable=False, index=True, server_default=text("''"))
    District = Column(CHAR(20), nullable=False, server_default=text("''"))
    Population = Column(INTEGER(11), nullable=False, server_default=text("0"))

    country = relationship('Country')


class Countrylanguage(Base):
    __tablename__ = 'countrylanguage'

    CountryCode = Column(ForeignKey('country.Code'), primary_key=True, nullable=False, index=True, server_default=text("''"))
    Language = Column(CHAR(30), primary_key=True, nullable=False, server_default=text("''"))
    IsOfficial = Column(Enum('T', 'F'), nullable=False, server_default=text("'F'"))
    Percentage = Column(DECIMAL(4, 1), nullable=False, server_default=text("0.0"))

    country = relationship('Country')
    

'''    
class city(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(35), index=True, unique=True)
    CountryCode = db.Column(db.String(3), index=True, unique=True)
    District = db.Column(db.String(20), index=True, unique=False)
    Population = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Name {}>'.format(self.Name)


-- world.country definition

CREATE TABLE `country` (
  `Code` char(3) NOT NULL DEFAULT '',
  `Name` char(52) NOT NULL DEFAULT '',
  `Continent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
  `Region` char(26) NOT NULL DEFAULT '',
  `SurfaceArea` decimal(10,2) NOT NULL DEFAULT 0.00,
  `IndepYear` smallint(6) DEFAULT NULL,
  `Population` int(11) NOT NULL DEFAULT 0,
  `LifeExpectancy` decimal(3,1) DEFAULT NULL,
  `GNP` decimal(10,2) DEFAULT NULL,
  `GNPOld` decimal(10,2) DEFAULT NULL,
  `LocalName` char(45) NOT NULL DEFAULT '',
  `GovernmentForm` char(45) NOT NULL DEFAULT '',
  `HeadOfState` char(60) DEFAULT NULL,
  `Capital` int(11) DEFAULT NULL,
  `Code2` char(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `city` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(35) NOT NULL DEFAULT '',
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `District` char(20) NOT NULL DEFAULT '',
  `Population` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`ID`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)
) ENGINE=InnoDB AUTO_INCREMENT=4080 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

## db.Model.metadata.tables['city']

class city(db.Model):
    __table__ = db.metadatas["world"].tables["city"]

    def __repr__(self):
        return '<City {}>'.format(self.Name)

class country(db.Model):
    __table__ = db.metadatas["world"].tables["country"]

    def __repr__(self):
        return '<Name {}>'.format(self.Name)
    
class country(db.Model):
    __table__ = db.metadatas["world"].tables["countrylanguage"]

    def __repr__(self):
        return '<Language {}>'.format(self.Language)
 
'''
