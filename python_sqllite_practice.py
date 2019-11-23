import psycopg2

def create():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr=conn.cursor()
    curr.execute("CREATE TABLE if not EXISTS store(idx INTEGER, item TEXT, quantity INTEGER, value REAL)")
    conn.commit()
    conn.close()

def insert(idx,item,quantity,value):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("INSERT INTO store VALUES(%s,%s,%s,%s)",(idx,item,quantity,value))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")
    rows=curr.fetchall()
    conn.close()
    return rows

def delete(idx):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("DELETE FROM store WHERE item=%s",(str(idx)))
    conn.commit()
    conn.close()

def update(idx,quantity,value):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Noorinbano' host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=%s,value=%s WHERE idx=%s",(quantity,value,idx))
    conn.commit()
    conn.close()

create()

insert(1,"item1",2,10)
insert(2,"item2",3,15)
update(2,7,25)
insert(3,"item3",4,20)
#print(view())
delete(1)
#print(view())