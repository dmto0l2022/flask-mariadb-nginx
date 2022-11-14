from flask import current_app as app
#from app import db
db = app.extensions['sqlalchemy'].db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class city(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(35), index=True, unique=True)
    CountryCode = db.Column(db.String(3), index=True, unique=True)
    District = db.Column(db.String(20), index=True, unique=False)
    Population = db.Column(db.Integer, index=True, unique=False)
)
    def __repr__(self):
        return '<Name {}>'.format(self.Name)
    
'''
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
