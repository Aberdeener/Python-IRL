import requests
import json
import gspread
import calendar
from oauth2client.service_account import ServiceAccountCredentials

response = requests.get("https://connect.monstercat.com/api/catalog/browse")
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Test123").sheet1

if response.status_code == 200:
    print("connected to api...")

    # future tadhg: we need to read json backwards
    print("reading json and inserting to table...")
    for song in response.json()['results']:

        values_list = sheet.col_values(3)
        if song['title'] in values_list:
            print("duplicate song " + song['title'] + " skipping...")
            continue

        print("adding " + song['title'] + "...")

        debutDateDay = song['debutDate'][8:10]
        debutDateYear = song['debutDate'][2:4]
        debutDateMonth = calendar.month_abbr[int(song['debutDate'][5:7])]

        debutDate = debutDateMonth + ' ' + debutDateDay + ' (' + debutDateYear + ')'

        row = [debutDate, song['genreSecondary'], song['title'], song['artistsTitle']]
        sheet.insert_row(row, 9)

    print("completed with no errors")

else:
    print("error communicating with monstercat api")
