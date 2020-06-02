import os
import psycopg2
import json
import csv
import time

ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

print(ELEPHANT_HOST)

dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)

def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    # saformatē pieslēgšanās parametrus
    # dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    # izveido pieslēgumu
    conn = psycopg2.connect(dsn)
    # izveido kursoru
    cur = conn.cursor()
    # aizsūta kursoram SQL vaicājumu
    cur.execute("SELECT version();")
    # pieprasa no kursora atbildi
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    # aizver kursoru
    cur.close()
    # aizver peislēgumu daubāzei
    conn.close()
    return result

def ierakstit(parametri):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql="""INSERT INTO izvele (vards,uzvards,izvele_id,datori_id,specdebates,specanglit,specfiloz,specpub,specpapangv,specpsih,specrobo,speckrv,padz_id1,padz_id2,padz_id3) 
        VALUES ({}) RETURNING nrpk;""" 
    cur.execute(sql.format(parametri))
    conn.commit()
    cur.close()
    conn.close()
    return 

def nolasit(parametri = 0):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    if parametri==0:
        kverijs='''SELECT izvele.nrpk, izvele.vards, izvele.uzvards, izvele.datums, grozi.nosaukums, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id ORDER BY nrpk ASC'''
        cur.execute(kverijs)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    elif parametri.izvele == 1:
        numurs = int(parametri.teksts)
        querry = '''SELECT * FROM (SELECT izvele.nrpk, izvele.vards, izvele.uzvards, izvele.datums, grozi.nosaukums, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id ORDER BY nrpk ASC) AS tabula WHERE tabula.nrpk='{}' '''.format(numurs)
        print(querry)
        cur.execute(querry)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    else:
        cur.execute('''SELECT * FROM (SELECT izvele.nrpk, izvele.vards, izvele.uzvards, izvele.datums, grozi.nosaukums, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id ORDER BY nrpk ASC) AS tabula WHERE tabula.uzvards LIKE '{}%' '''.format(parametri.teksts))
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    return r
