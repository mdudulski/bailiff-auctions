from data_downloads import *
from checkiflinkisactive import *
from add_coordinates import *
from filljs import *

def main():
    mycursor, mydb = initializedb()
    downloaddata(mycursor, mydb) # downloadsdata
    print('data are downloaded')
    checkifisactive(mycursor, mydb)
    print('all data are active')
    add_coordinates(mycursor,mydb)
    print('coordinates are added')
    filljs(mycursor,mydb)



if __name__ == "__main__":
    main()