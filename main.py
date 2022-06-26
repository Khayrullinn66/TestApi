
from a1range import A1Range
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import psycopg2
from config import host,user,password,db_name



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI'
SAMPLE_RANGE_NAME = 'Лист1'


service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

# Call the Sheets API
# result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                      range=SAMPLE_RANGE_NAME).execute()

# data_from_sheet = result.get('values', [])

array = {'values': [[45,1220096, 214, 06.01/2002], [34,6278290, 512, 16.09/2021]]}
range_ = A1Range.create_a1range_from_list('Лист1', 4, 1, array['values']).format()
response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=range_,
                          valueInputOption='USER_ENTERED',
                          body=array).execute()


try:
    # Подключаемся к базе
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
   # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] Error while working PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")




