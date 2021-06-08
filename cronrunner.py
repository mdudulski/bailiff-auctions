from data_downloads import *
from checkifisactive import *
from add_coordinates import *
from filljs import *
from to_columns import *

def main():

    mycursor, mydb = initializedb()
    downloaddata(mycursor, mydb) # downloadsdata
    to_columns(mycursor,mydb)
    print('data are converted to columns')
    checkifisactive(mycursor,mydb)
    print('all data are active')
    add_coordinates(mycursor,mydb)
    print('coordinates are added')
    filljs(mycursor,mydb)
    mydb.close()

    requests.get('https://hc-ping.com/101d7488-156a-47ac-b13f-08122c72bf38', timeout=10)
if __name__ == "__main__":
    main()

