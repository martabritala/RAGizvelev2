import datetime
import os
import psycopg2
from flask import Flask, g, render_template, request, redirect
import data
# from boto.s3.connection import S3Connection

app = Flask('app')

# class objekts:
#     def __init__(self, izvele, teksts):
#         self.izvele=izvele
#         self.teksts=teksts

@app.route('/')
def index_lapa():
    return render_template('index.html')

@app.route('/gatavs', methods=['POST', 'GET'])
def gatavs():
    if request.method=='POST':
        stundas = request.form.getlist('stunduskaits[]')
        print(stundas)
        print(request.form.getlist('izvele'))
        print(request.form['izvele'])
        return render_template('gatavs.html', stunduskaits=[36,36,36], vards=request.form['vards'], uzvards=request.form['uzvards'], programma=request.form['programma'], masivs=request.form.getlist('izvele[]'))
    else:
        return render_template('gatavs.html', klase10=32, klase11=30, klase12=18, vards='Jānis', uzvards='Bērziņš', programma=1, masivs=[30,18,13])

@app.route('/test')
def test():
    return data.test_connection()



@app.route('/test1/<ieraksts>')
def tests1(ieraksts):
    parametri="'{}','berziņš',1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,5,7".format(ieraksts)
    data.ierakstit(parametri)
    return data.test_connection()

