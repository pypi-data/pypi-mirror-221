from google.oauth2 import service_account
from googleapiclient.discovery import build


def load_credentials(credentials_file_full_path):
    return service_account.Credentials.from_service_account_file(credentials_file_full_path)


class Exporter():
    def __init__(self, spreadsheet_id:str, list_name:str, data:list, credentials_file_full_path="credentials.json"):
        super().__init__()
        self.spreadsheet_id = spreadsheet_id
        self.list_name = list_name
        self.data = data
        self.creds_file_path = credentials_file_full_path

        self.credentials = load_credentials(credentials_file_full_path)

    def export(self):
        print("exporting data ..")
        service = build('sheets', 'v4', credentials=self.credentials)

        # Spreadsheet ID - Obtain this from the URL of your Google Sheet
        spreadsheet_id = self.spreadsheet_id

        # Define the range where you want to insert the data (e.g., 'Sheet1!A1')
        range_name = self.list_name

        # Call the Sheets API to insert the data into the Google Sheet
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body={'values': self.data}
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")