from argparse import ArgumentParser
from src.postgresManagement import postgresManagement
from src.remoteQuery import retrieveDatabaseEntries

def main():
    parser = ArgumentParser(description='Icarus program to append bird detection to DB')
    parser.add_argument('host', type=str, description='RasPi IP Address')
    parser.add_argument('user', type=str, description='RasPi username')
    parser.add_argument('password', type=str, description='RasPi password')
    parser.add_argument('site_name', type=str, description='BirdNET station site name')
    parser.add_argument('db_file_name', type=str, 
                        description='/path/to/db/file.db')
    args = parser.parse_args()

    postgres = postgresManagement()
    query = retrieveDatabaseEntries()

    db_length = postgres.currentDBLength()
    new_entry_length = query.

    


if __name__ == '__main__':
    main()