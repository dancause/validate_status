import sqlite3
from datetime import datetime
import time

class Website:
    def __int__(self,number,link,date,status):
        self.number = number
        self.link = link
        self.date = date
        self.status = status


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/cms_db.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_url(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("""select * from url""")
        listes = []
        for row in cursor:
            p = Website(row[0],row[1],row[2],row[3], row[4])
            listes.append(p)
        return listes

    def save_log(self,link,status):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(("""insert into log ( link, date, status ) values (?,?,?)"""),(link, datetime.now(), status, ))
        connection.commit()

        