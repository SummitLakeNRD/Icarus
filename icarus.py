from argparse import ArgumentParser
from src.postgresManagement import postgresManagement
from src.remoteQuery import retrieveDatabaseEntries

def main():
    parser = ArgumentParser(description='Icarus program to append bird detection to DB')
    parser.add_argument('host', type=str)
    parser.add_argument('user', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('site_name', type=str)
    parser.add_argument('db_file_name', type=str)
    args = parser.parse_args()

    postgres = postgresManagement()
    query = remoteQuery()

    db_length = postgres.currentDBLength()
    new_entry_length = query.

    


if __name__ == '__main__':
    main()