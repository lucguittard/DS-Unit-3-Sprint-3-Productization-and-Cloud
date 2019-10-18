"""OpenAQ Air Quality Dashboard with Flask."""

import requests as r
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#from models import DB #for making a DB

request = r.get('https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25').json()

APP = Flask(__name__)

#DB.init_APP(APP)

#Pointing to where the DB is 
#APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
#DB.create_all()
#DB creation optional for SC


APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    date = DB.Column(DB.String(100))
    value = DB.Column(DB.Float, nullable=False)
    def __repr__(self):
        return "< Record {} >".format(self.value,self.date)

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()

    request = r.get('https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25').json()
    
    for i in request['results']:
        value = (i['value'])
        date = (i['date'])
        DB.session.add(Record(value=value,date=date))

    DB.session.commit()
    return 'Data refreshed!'

#function to populate the root
@APP.route('/')  #root route
def home():
    request = r.get('https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25').json()

    #make the lists to be used in tuple
    value = []
    date = []
    for i in request['results']:
        value.append(i['value'])
        date.append(i['date'])

    #combine the lists
    data_list = str(tuple(zip(value,date)))
    return data_list 

    #query the datatable
    filtered = Record.query.filter(Record.value >= 10).all()
    return filtered


if __name__ == '__main__':
    APP.run() 
