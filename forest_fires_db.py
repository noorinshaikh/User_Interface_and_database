import psycopg2

def connect():
    conn=psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr=conn.cursor()
    curr.execute("CREATE TABLE if not EXISTS cal_fires(id SERIAL, state varchar, city varchar,type varchar, size integer)")
    conn.commit()
    conn.close()

def insert(state,city,type,size):
    conn = psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("SELECT COUNT(*) FROM cal_fires")
    val=curr.fetchall()[0][0]
    curr.execute("INSERT INTO cal_fires (id,state,city,type,size) VALUES (%s,%s,%s,%s,%s)",(val,state,city,type,size))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("SELECT * FROM cal_fires")
    rows=curr.fetchall()
    conn.close()
    return rows

def delete(idx):
    conn = psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("DELETE FROM cal_fires WHERE id=%s",(str(idx)))
    conn.commit()
    conn.close()

def search(state,city,type,size):
    conn = psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("SELECT * FROM cal_fires WHERE state=%s OR city=%s OR type=%s OR size=%s ",(state,city,type,size))
    rows=curr.fetchall()
    conn.close()
    return rows

def update(id,state,city,type,size):
    conn = psycopg2.connect("dbname='california_forest_fires' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("UPDATE cal_fires SET state=%s,city=%s,type=%s,size=%s WHERE id=%s",(state,city,type,size,id))
    conn.commit()
    conn.close()

connect()