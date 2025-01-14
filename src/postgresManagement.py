import psycopg
import pickle
from uuid import uuid4

class postgresManagement:
    def __init__(self):
        self.dbname = "<DBNAME>",
        self.user = "<USER>",
        self.password = "<PASSWORD>",
        self.host = "<HOST>",
        self.port = "<PORT>"

    def currentDBLength(self):
        # Create connection to Postgres DB
        with psycopg.connect(
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port) as conn:

            # Create connection pipeline for commands
            with conn.cursor() as cur:

                # Execute SQL command and store values
                cur.execute(
                    """SELECT COUNT(*) FROM 
                    <TABLE_NAME>;""")
                row_count = cur.fetchall()[0][0]
        return row_count


    def appendNewEntries(self):

    
    def updatedDBLength(self):
        # Create connection to Postgres DB
        with psycopg.connect(
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port) as conn:

            # Create connection pipeline for commands
            with conn.cursor() as cur:

                # Execute SQL command and store values
                cur.execute(
                    """SELECT COUNT(*) FROM 
                    <TABLE_NAME> WHERE Site_Name = self""")
                row_count = cur.fetchall()[0][0]