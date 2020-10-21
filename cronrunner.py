#!/home/mateusz/PycharmProjects/bailiff-auctions/venv/bin/python
from data_downloads import *
from checkiflinkisactive import *
from add_coordinates import *
from filljs import *
from to_columns import *

def main():
    mycursor, mydb = initializedb()
    print('database is initialized')
    downloaddata(mycursor, mydb) # downloadsdata
    print('data are downloaded')
    to_columns(mycursor,mydb)
    print('data are converted to columns')

    checkifisactive(mycursor, mydb)
    print('all data are active')
    mycursor, mydb = initializedb()
    add_coordinates(mycursor,mydb)
    print('coordinates are added')
    filljs(mycursor,mydb)
    mydb.close()


if __name__ == "__main__":
    main()