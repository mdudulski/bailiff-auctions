import herepy
from geopy import Nominatim
from database_set import *
from config import *



def add_coordinates(mycursor,mydb):
    locator = Nominatim(user_agent='myGeocoder')

    latitude = ''
    longitude = ''


    query = "SELECT id,address FROM bailiff_auctions_fields where latitude  is null or latitude = ''"
    mycursor.execute(query)
    result = mycursor.fetchall()

    for row in result:
        id = row[0]
        address = row[1]
        try:
            geocoderApi = herepy.GeocoderApi(herepykey)
            response = geocoderApi.free_form(address)

            data = response.as_dict()

            data = data['items'][0]['position']

            latitude = data['lat']
            print(latitude)
            longitude = data['lng']
            print(longitude)

        except Exception as e:
            latitude = 'NULL'
            longitude = 'NULL'

        sql = "UPDATE bailiff_auctions_fields SET latitude = '" + str(latitude) + "',longitude = '" + str(
            longitude) + "' WHERE id ='" + str(id) + "'"
        insert_data(mycursor, sql)

    mydb.commit()
    mydb.close()