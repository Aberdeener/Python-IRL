import requests
import gspread
import calendar
from oauth2client.service_account import ServiceAccountCredentials

response = requests.get("https://connect.monstercat.com/api/catalog/browse")
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Test123").sheet1

if response.status_code == 200:

    print("connected... inserting to sheet...")

    for song in sorted(response.json()['results'], key=lambda i: i['debutDate']):

        songNames = sheet.col_values(3)
        if song['title'] in songNames:
            print("duplicate song " + song['title'] + " skipping...")
            continue
        if song['artistsTitle'] == "Monstercat":
            print("skipping " + song['title'] + "...")
            continue

        print("adding " + song['title'] + "...")

        debutDateDay = song['debutDate'][8:10]
        debutDateYear = song['debutDate'][2:4]
        debutDateMonth = calendar.month_abbr[int(song['debutDate'][5:7])]
        debutDate = debutDateMonth + ' ' + debutDateDay + ' (' + debutDateYear + ')'

        try:
            artists = song['artists'][0]['name'] + ', ' + song['artists'][1]['name']
            feature = song['artists'][2]['name']
        except IndexError:
            artists = song['artistsTitle']
            feature = ''

        row = ['', debutDate, song['genreSecondary'], '', song['title'], artists,
               feature, '', song['release']['title']]
        sheet.insert_row(row, 13)

    print("completed with no errors")

else:
    print("error communicating with monstercat api")
