from database_set import *
from bs4 import BeautifulSoup
import requests
from itertools import chain
from config import *


def get_data(id, mycursor):
    try:
        source = requests.get(website_link + str(id) + '').text
        soup = BeautifulSoup(source, 'lxml')
        text = soup.find('div', class_='schema-preview').text
        category = soup.find('div', class_='row').text
        category = category.replace('Kategoria', '')

        query = "INSERT INTO bailiff_auctions_text (id,category, auction_text) VALUES ('" + str(
            id) + "','" + category + "','" + text + "')"

        try:
            insert_data(mycursor, query)

        except Exception as e:
            print('the record is already in the database')


    except Exception as e:
        print('link empty')


def initializedb():
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    create_table(mycursor,
                 'CREATE TABLE IF NOT EXISTS bailiff_auctions_text (id INT NOT NULL,category VARCHAR(255), auction_text VARCHAR(20000) NOT NULL,timestamp TIMESTAMP ,is_active tinyint(1) default 1, PRIMARY KEY (id))')

    return mycursor, mydb


def countstart(mycursor):
    query = "SELECT MAX(id) FROM bailiff_auctions_text order by id desc"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result[0][0] - 100







def main():
    mycursor, mydb = initializedb()

    start_id = countstart(mycursor)
    end_id = start_id + 5000
    start_id = 517792
    end_id = 517824
    query = "SELECT id FROM bailiff_auctions_fields"

    mycursor.execute(query)

    result = mycursor.fetchall()
    mylist = list(chain.from_iterable(result))
    print(mylist)

    for id in range(start_id, end_id + 1):
        print(id)
        if id in mylist:
            print('the record is already in the database (for)')
        else:
            get_data(id, mycursor)
            if id % 100 == 0:
                mydb.commit()

    mydb.commit()
    mydb.close()


if __name__ == "__main__":
    main()
