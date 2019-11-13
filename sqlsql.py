import mysql.connector

currentTime = 99

db_connection = mysql.connector.connect(
    host='localhost',
    user='user',
    password='pass',
    auth_plugin='mysql_native_password',
    buffered = True
)

print(db_connection)
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE DATABASE IF NOT EXISTS microbits")
db_cursor.execute("USE microbits")
db_cursor.execute("CREATE TABLE IF NOT EXISTS a (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS b (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS c (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS d (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS e (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS f (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS g (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS h (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS i (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS j (s_id CHAR(4), temp VARCHAR(10), light VARCHAR(10), time VARCHAR(10), date VARCHAR(15))")
db_cursor.execute("SHOW TABLES")

def get_A():
    db_cursor.execute("SELECT temp, light, time, date FROM a LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_B():
    db_cursor.execute("SELECT temp, light, time, date FROM b LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_C():
    db_cursor.execute("SELECT temp, light, time, date FROM c LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_D():
    db_cursor.execute("SELECT temp, light, time, date FROM d LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_E():
    db_cursor.execute("SELECT temp, light, time, date FROM e LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_F():
    db_cursor.execute("SELECT temp, light, time, date FROM f LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_G():
    db_cursor.execute("SELECT temp, light, time, date FROM g LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_H():
    db_cursor.execute("SELECT temp, light, time, date FROM h LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_I():
    db_cursor.execute("SELECT temp, light, time, date FROM i LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_J():
    db_cursor.execute("SELECT temp, light, time, date FROM j LIMIT 120;")
    result = db_cursor.fetchall()
    return result

def get_lastA():
    db_cursor.execute("SELECT temp, light, time, date FROM a ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastB():
    db_cursor.execute("SELECT temp, light, time, date FROM b ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastC():
    db_cursor.execute("SELECT temp, light, time, date FROM c ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastD():
    db_cursor.execute("SELECT temp, light, time, date FROM d ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastE():
    db_cursor.execute("SELECT temp, light, time, date FROM e ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastF():
    db_cursor.execute("SELECT temp, light, time, date FROM f ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastG():
    db_cursor.execute("SELECT temp, light, time, date FROM g ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastH():
    db_cursor.execute("SELECT temp, light, time, date FROM h ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastI():
    db_cursor.execute("SELECT temp, light, time, date FROM i ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result

def get_lastJ():
    db_cursor.execute("SELECT temp, light, time, date FROM j ORDER BY time DESC LIMIT 1;")
    result = db_cursor.fetchall()
    return result


def cleanTable_A():
    db_cursor.execute("SELECT COUNT(s_id) FROM a")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM a LIMIT %s", (toRemove,))

def cleanTable_B():
    db_cursor.execute("SELECT COUNT(s_id) FROM b")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM b LIMIT %s", (toRemove,))

def cleanTable_C():
    db_cursor.execute("SELECT COUNT(s_id) FROM C")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM c LIMIT %s", (toRemove,))

def cleanTable_D():
    db_cursor.execute("SELECT COUNT(s_id) FROM d")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM d LIMIT %s", (toRemove,))

def cleanTable_E():
    db_cursor.execute("SELECT COUNT(s_id) FROM e")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM e LIMIT %s", (toRemove,))

def cleanTable_F():
    db_cursor.execute("SELECT COUNT(s_id) FROM f")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM f LIMIT %s", (toRemove,))

def cleanTable_G():
    db_cursor.execute("SELECT COUNT(s_id) FROM g")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM g LIMIT %s", (toRemove,))

def cleanTable_H():
    db_cursor.execute("SELECT COUNT(s_id) FROM h")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM h LIMIT %s", (toRemove,))

def cleanTable_I():
    db_cursor.execute("SELECT COUNT(s_id) FROM i")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM i LIMIT %s", (toRemove,))

def cleanTable_J():
    db_cursor.execute("SELECT COUNT(s_id) FROM j")
    result = db_cursor.fetchall()
    size = result[0]
    size = size[0]
    toRemove = 0
    if(size > 120):
        toRemove = size-120
    db_cursor.execute("DELETE FROM j LIMIT %s", (toRemove,))

def clean_All():
    cleanTable_A()
    cleanTable_B()
    cleanTable_C()
    cleanTable_D()
    cleanTable_E()
    cleanTable_F()
    cleanTable_G()
    cleanTable_H()
    cleanTable_I()
    cleanTable_J()

class lists:
    alist = [99]
    blist = [99]
    clist = [99]
    dlist = [99]
    elist = [99]
    flist = [99]
    glist = [99]
    hlist = [99]
    ilist = [99]
    jlist = [99]


def table_A(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.alist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.alist[0] == 99 or newTime-lists.alist[0] >= 5):
        db_cursor.execute("INSERT INTO a (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE a SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.alist[0] = newTime

def table_B(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.blist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.blist[0] == 99 or newTime-lists.blist[0] >= 5):
        db_cursor.execute("INSERT INTO b (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE b SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.blist[0] = newTime


def table_C(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.clist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.clist[0] == 99 or newTime-lists.clist[0] >= 5):
        db_cursor.execute("INSERT INTO c (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE c SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.clist[0] = newTime

def table_D(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.dlist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.dlist[0] == 99 or newTime-lists.dlist[0] >= 5):
        db_cursor.execute("INSERT INTO d (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE d SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.dlist[0] = newTime

def table_E(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.elist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.elist[0] == 99 or newTime-lists.elist[0] >= 5):
        db_cursor.execute("INSERT INTO e (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE e SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.elist[0] = newTime

def table_F(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.flist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.flist[0] == 99 or newTime-lists.flist[0] >= 5):
        db_cursor.execute("INSERT INTO f (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE f SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.flist[0] = newTime

def table_G(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.glist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.glist[0] == 99 or newTime-lists.glist[0] >= 5):
        db_cursor.execute("INSERT INTO g (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE g SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.glist[0] = newTime

def table_H(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.hlist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.hlist[0] == 99 or newTime-lists.hlist[0] >= 5):
        db_cursor.execute("INSERT INTO h (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE h SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.hlist[0] = newTime

def table_I(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.ilist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.ilist[0] == 99 or newTime-lists.ilist[0] >= 5):
        db_cursor.execute("INSERT INTO i (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE i SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.ilist[0] = newTime

def table_J(sensor, temp, light, time, date):
    newTime = int(time[3] + time[4])

    if(lists.jlist[0] >=56):
        if(newTime <= 5):
            newTime += 60
    if(lists.jlist[0] == 99 or newTime-lists.jlist[0] >= 5):
        db_cursor.execute("INSERT INTO j (s_id, temp, light, time, date) VALUES(%s, %s, %s, %s, %s)", (sensor, temp, light, time, date))
        db_cursor.execute("UPDATE j SET date = REPLACE(date, '\n', '');")
        db_connection.commit()
        lists.jlist[0] = newTime
    

