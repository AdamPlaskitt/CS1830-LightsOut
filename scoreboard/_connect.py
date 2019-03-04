import gspread
from oauth2client.service_account import ServiceAccountCredentials


# attempt a connection to google spreadsheet
def connect():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # User credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name('cs-pixel-game-db-efd319aa286d.json', scope)
    gc = gspread.authorize(credentials)

    # open & return spreadsheet
    wks = gc.open("scoreboard").sheet1
    return wks
