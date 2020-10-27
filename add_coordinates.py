import herepy
from geopy import Nominatim
from database_set import *
from config import *
from sql_queries import select_address_from_fields, update_latitude_fields


def add_coordinates(mycursor,mydb):
    query = select_address_from_fields()
    #query = "SELECT id,address FROM bailiff_auctions_fields where latitude = 'None'"
    print(query)
    mycursor.execute(query)
    result = mycursor.fetchall()

    for row in result:
        auction_id = row[0]
        address = row[1]
        try:
            geocoderApi = herepy.GeocoderApi(herepykey)
            response = geocoderApi.free_form(address)
            data = response.as_dict()
            data = data['items'][0]['position']
            latitude = str(data['lat'])
            longitude = str(data['lng'])

        except Exception as err:
            latitude = None
            longitude = None

        sql = update_latitude_fields(auction_id, latitude, longitude)
        insert_data(mycursor, sql)

    mydb.commit()
