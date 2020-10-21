from database_set import *
from data_quality import *
from config import *

def property(id, category, text,mycursor):
    address = find_address(text)
    estimated_sum = find_estimated_sum(text)
    starting_price = find_starting_price(text)
    auction_date = find_auction_date(text)
    link = website_link + str(id)
    query = "INSERT INTO bailiff_auctions_fields (id,category,address,estimated_sum,starting_price,auction_date,link) VALUES ('" + str(id) + "','" + category + "','" + address + "','" + estimated_sum + "','" + starting_price + "','" + auction_date + "','" + link + "')"
    insert_data(mycursor, query)

def to_columns(mycursor,mydb):

    create_table(mycursor,
                 'CREATE TABLE IF NOT EXISTS bailiff_auctions_fields (id INT NOT NULL,category VARCHAR(255), address VARCHAR(255),estimated_sum VARCHAR(255),starting_price VARCHAR(255),auction_date VARCHAR(255),latitude VARCHAR(255),longitude VARCHAR(255),link VARCHAR(255),timestamp TIMESTAMP ,is_active tinyint(1) default 1, PRIMARY KEY (id))')

    query = "SELECT bat.* FROM bailiff_auctions_text as bat LEFT JOIN bailiff_auctions_fields as baf on bat.id=baf.id where bat.category in ('nieruchomości','mieszkania','domy','grunty','garaże, miejsca postojowe','lokale użytkowe','magazyny i hale') and baf.id is null order by bat.id asc"

    mycursor.execute(query)
    result = mycursor.fetchall()
    for row in result:

        id = row[0]
        category = row[1]
        print(str(id) + ' ' + category)
        text = row[2]
        property(id, category, text, mycursor)
        if row[0] % 100 == 0:
            mydb.commit()
    mydb.commit()
