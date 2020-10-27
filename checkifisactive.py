from itertools import chain
from bs4 import BeautifulSoup
import requests
from config import website_link
from sql_queries import select_auctions_fields_is_active, update_deactivate_fields, select_ids_from_text


def checkifisactive(mycursor, mydb):
    query = select_auctions_fields_is_active()
    mycursor.execute(query)
    result = mycursor.fetchall()
    mylist = list(chain.from_iterable(result))

    for auction_id in mylist:
        try:
            source = requests.get(website_link + str(auction_id) + '').text
            soup = BeautifulSoup(source, 'lxml')
            soup.find('div', class_='schema-preview').text
            print(str(auction_id) + ' link is ok')
            mydb.commit()
        except AttributeError as err:
            print(str(auction_id) + ' i did update ' + ' ' + str(err))
            querymax = update_deactivate_fields(auction_id)
            mycursor.execute(querymax)
            mydb.commit()
