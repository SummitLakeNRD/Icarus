import os
import sqlite3
from paramiko import SSHClient
from scp import SCPClient

class retrieveDatabaseEntries:
    def __init__(self, host, username, password, site_name, db_file_name):
        self.host = host
        self.username = username
        self.password = password
        self.site_name = site_name
        self.db_file_name = db_file_name

    def retrieveDBFile(self):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(hostname = self.host, 
                    port = 'port', # Might get rid of port since its LAN application
                    username = self.username,
                    password = self.password)

        scp = SCPClient(ssh.get_transport())
        scp.get(os.path.join(self.db_file_name), 
                os.path.join(os.getcwd(), 'src'))
        scp.close()

    def remoteDBlegnth(self):
        con = sqlite3.connect(os.path.join(os.getcwd(), 'src', 'birds.db'))
        cur = con.cursor()
        # Might need to add WHERE clause for site name
        # Also change '10' to n-value for diff
        res = cur.execute("""SELECT Date,Time,Sci_Name,Com_Name,
                          Confidence,Lat,Lon from detections 
                          ORDER BY rowid DESC LIMIT 10""")
        return res.reverse()

