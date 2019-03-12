try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    print("ERROR: Please ensure that both the gspread and oauth2client packages are installed")
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
THIS_CREDENTIALS = '{DIR}{conn}{name}'.format(DIR=THIS_DIR, conn='\\', name='cs-pixel-game-db-efd319aa286d.json')


# attempt a connection to google spreadsheet
def connect():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # User credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(THIS_CREDENTIALS, scope)
    gc = gspread.authorize(credentials)

    # open & return spreadsheet
    wks = gc.open("scoreboard").sheet1
    return wks
