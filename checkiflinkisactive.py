from data_downloads import *

def checkifisactive(mycursor,mydb):


    query = "SELECT id FROM bailiff_auctions_fields where is_active = 1"

    mycursor.execute(query)

    result = mycursor.fetchall()
    mylist = list(chain.from_iterable(result))
    print(mylist)



    for iter in mylist:
        try:
            print(iter)
            source =requests.get(website_link + str(iter) + '').text
            soup = BeautifulSoup(source, 'lxml')
            text = soup.find('div', class_='schema-preview').text
            print('link is ok')

        except:
            print('I did update '+ str(iter))
            querymax = "UPDATE bailiff_auctions_fields SET is_active = 0 WHERE id = "+str(iter)
            mycursor.execute(querymax)
            if iter % 100 == 0:
                mydb.commit()

    mydb.commit()
    mydb.close()




mycursor, mydb = initializedb()
checkifisactive(mycursor,mydb)
