import psycopg
from uuid import uuid4

class postgresManagement:
    def __init__(self, dbname, user, password, host, port, site_name):
        # Enter PostgreSQL database information here
        self.dbname = dbname,
        self.user = user,
        self.password = password,
        self.host = host,
        self.port = port
        self.site_name = site_name

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
                cur.execute("SELECT COUNT(*) FROM <TABLE_NAME>")
                row_count = cur.fetchall()[0][0]

            # Close postgres connection
            conn.close()
        return row_count

    def appendNewEntries(self, bird_list):
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
                cur.executemany(
                    """INSERT INTO <TABLE_NAME> 
                    (uuid, Date, Time, Sci_Name, Com_Name, Confidence,
                     Lat, Lon, Cutoff, Week, Sens, Overlap, Site_Name) VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    uuid4(), bird_list[0], bird_list[1], bird_list[2],
                    bird_list[3], bird_list[4], bird_list[5], bird_list[6],
                    bird_list[7], bird_list[8], bird_list[9], bird_list[10], 
                    bird_list[11], self.site_name)
                
            # Close postgres connection    
            conn.close()

 