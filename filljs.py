from database_set import *
from config import *
import json
import ftplib

def filljs(mycursor,mydb):

    eqfeed_callback = {}
    eqfeed_callback['properties'] = []


    query = "SELECT id,link,latitude,longitude,category,estimated_sum,auction_date FROM bailiff_auctions_fields where latitude !='brak' and is_active!=0"
    mycursor.execute(query)
    result = mycursor.fetchall()

    for row in result:

        id = row[0]
        print(id)
        link = row[1]
        latitude = row[2]
        longitude = row[3]
        category = row[4]
        estimated_sum = row[5]
        auction_date = row[6]

        eqfeed_callback['properties'].append({
            'id': id,
            'url': link,
            'lat': latitude,
            'long': longitude,
            'category' : category,
            'estimated_sum': estimated_sum,
            'auction_date': auction_date
        })


    with open('mydata.js', 'w', encoding='utf-8') as out_file:
        out_file.write('eqfeed_callback( %s);' % json.dumps(eqfeed_callback))


    session = ftplib.FTP(ftp, ftp_login, ftp_password)

    session.cwd(ftp_folder)

    file = open('mydata.js', 'rb')  # file to send

    try:
        session.delete('mydata.js')


    except:
        print('nie ma pliku')

    session.storbinary('STOR mydata.js', file)  # send the file

    file.close()  # close file and FTP
    session.quit()