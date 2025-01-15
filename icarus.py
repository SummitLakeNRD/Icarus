from argparse import ArgumentParser
from src.postgresManagement import postgresManagement
from src.remoteQuery import remoteFetch


def main():
    parser = ArgumentParser(description='Icarus program to append bird detection to DB')
    parser.add_argument('host', type=str, help='RasPi IP Address')
    parser.add_argument('user', type=str, help='RasPi username')
    parser.add_argument('password', type=str, help='RasPi password')
    parser.add_argument('db_file_name', type=str, help='/path/to/db/file.db')
    parser.add_argument('site_name', type=str, help='BirdNET station site name')
    args = parser.parse_args()

    # Pass in PostgreSQL database information to establish connectioni
    # Will need to pass in DB specific values
    postgres = postgresManagement("<DBNAME>", "<USER>", "<PASSWORD>", 
                                  "<HOST>", "<PORT>", "<SITE>")
    # Pass in sqlite3 db parameters from CLI arguments
    remote = remoteFetch(args.host, args.user, args.password,
                         args.site_name, args.db_file_name) 

    remote.retrieveDBFile()
    new_entry_length = remote.remoteDBlegnth()
    #db_length = postgres.currentDBLength()
    db_length = 3400 # For testing
    new_append_list = remote.DBQuery(db_length, new_entry_length)
    print(new_append_list[0])
    #postgres.appendNewEntries(new_append_list)

    
if __name__ == '__main__':
    main()
