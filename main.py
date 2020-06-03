import datetime
import os
import psycopg2
from flask import Flask, g, render_template, request, redirect
import data
# from boto.s3.connection import S3Connection

app = Flask('app')

class objekts:
    def __init__(self, izvele, teksts):
        self.izvele=izvele
        self.teksts=teksts

@app.route('/')
def index_lapa():
    return render_template('index.html')

@app.route('/gatavs')
def gatavs():
    return render_template('gatavs.html')

@app.route('/test')
def test():
    return data.test_connection()

@app.route('/rezultati', methods=['POST', 'GET'])
def rezultati():
    if request.method == 'POST':
        ManaIzvele=int(request.form['izvele'])
        MansTeksts=request.form['teksts']
        MansObjekts=objekts(ManaIzvele,MansTeksts)
        rezultats=data.nolasit(MansObjekts)
    else:
        rezultats=data.nolasit()
    return render_template('rezultati.html', linijas=rezultats)

@app.route('/test2/<izvele1>/<teksts1>')
def test2(izvele1, teksts1):
    izvele1=int(izvele1)
    rezultats=objekts(izvele1, teksts1)
    # rezultats.teksts=teksts
    # rezultats.izvele=izvele
    return ''.join(map(str,data.nolasit(rezultats)))

@app.route('/test1/<ieraksts>')
def tests1(ieraksts):
    parametri="'{}','berziņš',1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,5,7".format(ieraksts)
    data.ierakstit(parametri)
    return data.test_connection()

@app.errorhandler(500)
def servererror():
    return redirect('/rezultati')