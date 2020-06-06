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

@app.route('/gatavs')
def gatavs():
    return render_template('gatavs.html')

@app.route('/test')
def test():
    return data.test_connection()



@app.route('/test1/<ieraksts>')
def tests1(ieraksts):
    parametri="'{}','berziņš',1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,5,7".format(ieraksts)
    data.ierakstit(parametri)
    return data.test_connection()

