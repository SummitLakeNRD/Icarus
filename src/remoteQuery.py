import os
import sqlite3
from paramiko import SSHClient
from scp import SCPClient

class remoteFetch:
    def __init__(self, host, username, password, site_name, db_file_path):
        self.host = host
        self.username = username
        self.password = password
        self.site_name = site_name
        self.db_file_path = db_file_path

    def retrieveDBFile(self):
        # Create ssh tunnel
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(hostname = self.host, 
                    username = self.username,
                    password = self.password)
        
        # Initialize & execute SCP of file
        scp = SCPClient(ssh.get_transport())
        scp.get(os.path.join(self.db_file_path), 
                os.path.join(os.getcwd(), 'src', 
                             self.site_name + '_birds.db'))
        
        # Close ssh connection
        scp.close()

    def remoteDBlegnth(self):
        # Create connection to sqlite3 DB
        con = sqlite3.connect(os.path.join(os.getcwd(), 'src', 
                                           self.site_name + '_birds.db'))
        cur = con.cursor()

        # Grab number of observations from table
        res = cur.execute("""SELECT COUNT(*) FROM detections""").fetchall()

        # Close sqlite3 connection
        con.close()
        return res[0][0] # returns INT of db table length
    
    def DBQuery(self, currentDB_length, updatedDB_length):
        query_length = updatedDB_length - currentDB_length
        con = sqlite3.connect(os.path.join(os.getcwd(), 'src', self.site_name + 
                                           '_' + 'birds.db'))
        cur = con.cursor()
        res = cur.execute("""SELECT Date, Date, Time, Sci_Name, Com_Name, 
                          Confidence, Lat, Lon, Cutoff, Week, Sens, Overlap
                          FROM detections ORDER BY rowid DESC LIMIT ?""", 
                          [query_length]).fetchall()
        con.close()
        # Note cannot use .reverse() method as list may be too large
        return res[::-1]