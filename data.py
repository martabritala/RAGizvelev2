import os
import psycopg2
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
        cur.execute('''SELECT * FROM izvele''')
    elif parametri.izvele == 1:
        cur.execute('''SELECT * FROM izvele WHERE nrpk={parametri.teksts}''')
    else:
        cur.execute('''SELECT * FROM izvele WHERE uzvards LIKE {parametri.teksts}''')
    return cur.fetchall()
