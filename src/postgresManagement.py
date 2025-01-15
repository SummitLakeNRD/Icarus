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
        # List comprehension to add site name to end of list tuples
        bird_list = [tuple(list(element) + [self.site_name]) for element in bird_list]

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
                    (Date, Time, Sci_Name, Com_Name, Confidence,
                     Lat, Lon, Cutoff, Week, Sens, Overlap, Site_Name) VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    bird_list)
                
            # Commit changes 
            conn.commit()    
                
            # Close postgres connection    
            cur.close()
            conn.close()

 