# Python-IRL
In an effort to learn the basics of python, I asked my friends what they wish they could automate on their computer

## netflix.py
Requested to open Netflix on login (assuming Windows enviroment)
1. Download netflix.py to Desktop.
2. Use windows' task scheduler to schedule script (C:\Users\{NAME}\Desktop\netflix.py) on login (afaik no way in python to load script on boot without 3rd party).

## mega-monstercat-sheet.py
Requested to scan [Monstercat's API](https://connect.monstercat.com/api/catalog/browse) every 12 hours, collect new songs and add to a Google Sheets sheet.
1. Download mega-monstercat-sheet.py to Desktop.
2. Install dependancies: `requests`, `json`, `gspread`, `calendar`, `oauth2client.service_account`.
3. Connect to Google API as explained [here](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html).
4. Edit name of sheet in file.
5. (Optional) Use cronjob to run every 12 hours.
