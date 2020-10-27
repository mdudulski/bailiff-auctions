from data_quality import find_address, find_estimated_sum, find_starting_price, find_auction_date
from config import website_link
from sql_queries import insert_bailiff_auctions_fields, select_auctions_text_left_join_fields


def get_data_from_text(auction_id, category, text, mycursor):
    address = find_address(text)
    estimated_sum = find_estimated_sum(text)
    starting_price = find_starting_price(text)
    auction_date = find_auction_date(text)
    link = website_link + str(auction_id)
    query = insert_bailiff_auctions_fields(auction_id, category, address, estimated_sum
                                           , starting_price, auction_date, link)
    mycursor.execute(query)


def to_columns(mycursor, mydb):
    query = select_auctions_text_left_join_fields()
    mycursor.execute(query)
    result = mycursor.fetchall()
    for row in result:
        auction_id = row[0]
        category = row[1]
        print(str(auction_id) + ' ' + category)
        text = row[2]
        get_data_from_text(auction_id, category, text, mycursor)
        mydb.commit()
