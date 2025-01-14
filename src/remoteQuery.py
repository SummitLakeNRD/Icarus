import os
import sqlite3
import paramiko
from scp import SCPClient

class retrieveDatabaseEntries:
    def __init__(self, host, username, password, site_name, db_file_name):
        self.host = host
        self.username = username
        self.password = password
        self.site_name = site_name
        self.db_file_name = db_file_name

    def remoteDBlegnth(self):
        db_filename = self.site_name + "_" + self.db_file_name
        con = sqlite3.connect("")
        return db_length

        res = cur.execute("""SELECT Date,Time,Sci_Name,Com_Name,
                          Confidence,Lat,Lon from detections 
                          ORDER BY rowid DESC LIMIT 10""")

