from itertools import chain
import requests
import mysql.connector
from bs4 import BeautifulSoup
from config import website_link, elements_to_crawl
from database_set import insert_data, connect_to_database, create_table
from sql_queries import insert_bailiff_auctions_text, create_bailiff_auctions_text, \
    create_bailiff_auctions_fields, select_ids_from_text, select_max_id_from_fields


def get_data(auction_id, mycursor):
    try:
        source = requests.get(website_link + str(auction_id) + '').text
        soup = BeautifulSoup(source, 'lxml')
        text = soup.find('div', class_='schema-preview').text
        category = soup.find('div', class_='row').text
        category = category.replace('Kategoria', '')
        query = insert_bailiff_auctions_text(auction_id, category, text)
        try:
            insert_data(mycursor, query)

        except mysql.connector.Error as err:
            print("The record is already in database: {}".format(err))



    except AttributeError as err:
        print(str(auction_id) + " Link is empty: {}".format(err))


def initializedb():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    create_table(mycursor, create_bailiff_auctions_text())
    create_table(mycursor, create_bailiff_auctions_fields())
    print('database is initialized')

    return mycursor, mydb


def get_start_id(mycursor):
    # get start_id to website crawl
    query = select_max_id_from_fields()
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result[0][0] - 100


def downloaddata(mycursor, mydb):
    start_id = get_start_id(mycursor)
    end_id = start_id + elements_to_crawl
    query = select_ids_from_text()
    mycursor.execute(query)
    result = mycursor.fetchall()
    id_list = list(chain.from_iterable(result))
    counter = 0
    for auction_id in range(start_id, end_id + 1):
        if auction_id in id_list:
            print(str(auction_id) + 'the record is already in the database (for)')
        else:
            get_data(auction_id, mycursor)
            if counter%50==0:
                mydb.commit()
        counter+=1

    print('text data are downloaded')
