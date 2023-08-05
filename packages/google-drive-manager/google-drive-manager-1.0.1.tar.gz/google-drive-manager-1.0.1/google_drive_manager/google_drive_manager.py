import os.path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class SpreadSheetManager:
    creds = None
    service = None
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly',
              'https://www.googleapis.com/auth/drive']

    # for AWS
    def get_service(self, api_name, api_version, scopes, key_file):
        """Get a service that communicates to a Google API.

        Args:
            self : self
            api_name: The name of the api to connect to.
            api_version: The api version to connect to.
            scopes: A list auth scopes to authorize for the application.
            key_file: A valid service account JSON key file.

        Returns:
            A service that is connected to the specified API.
        """

        # Build the service object.
        credentials = service_account.Credentials.from_service_account_info(key_file)
        scoped_credentials = credentials.with_scopes(scopes)
        self.service = build(api_name, api_version, credentials=scoped_credentials)

    def connect(self):
        """Connect to Google Drive
        """
        
        ##### Connect LOCAL
        # token_path = './token.json'
        # # creds_path = './credentials_google_local.json'
        
        # # Create credentials / To comment for AWS Lambda
        # if os.path.exists(token_path):
        #     self.creds = Credentials.from_authorized_user_file(
        #         token_path, self.SCOPES)
        # if not self.creds or not self.creds.valid:
        #     if self.creds and self.creds.expired and self.creds.refresh_token:
        #         self.creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file(
        #             creds_path, self.SCOPES)
        #         self.creds = flow.run_local_server(port=0)
        #     with open(token_path, 'w', encoding="utf-8") as token:
        #         token.write(self.creds.to_json())

        ##### Connect AWS
        credentials = json.loads(os.environ['GOOGLE_CREDENTIALS'])
        credentials = Credentials.from_service_account_info(credentials, scopes=self.SCOPES)
        self.service = build("sheets", "v4", credentials=credentials)


    def getAllValuesFromSheet(self, spreadsheet_id, sheet_name, prange):
        """Get information from Google Drive

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            sheet_name (str): name of the sheet
            prange (str): Range of the data

        Returns:
            res: information from the sheet_name of the spreadsheet_id
        """
        res = []
        if not self.service:
            self.connect()

        sheet_range = str(sheet_name)+'!'+str(prange)
        request = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=sheet_range)
        response = request.execute()
        if 'values' in response:
            for value in response['values']:
                res.append(value)

        return res
    
    def setColData(self,spreadsheet_id,sheet_name,col_name,col_data):
        """Set information in Google Drive file

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            sheet_name (str): name of the sheet
            col_name (str): name of the column
            col_data (list) : list of data to set

        Returns:
            res: information from the sheet_name of the spreadsheet_id
        """
        if not self.service:
            self.connect()
        
        body = {
            "majorDimension": "COLUMNS",
            "values": [col_data]
        }
        sheetRange = str(sheet_name)+'!'+str(col_name)
        
        result = self.service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=sheetRange,
        valueInputOption='RAW',
        body=body).execute()

        return result
    
    def getSheetId(self, spreadsheet_id, sheet_name):
        """Get Sheet ID from un file

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            sheet_name (str): name of the sheet

        Returns:
            res: information from the sheet_name of the spreadsheet_id
        """

        if not self.service:
            self.connect()
        
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = spreadsheet.get('sheets', [])
        for sheet in sheets:
            properties = sheet.get('properties', {})
            if properties.get('title') == sheet_name:
                return properties.get('sheetId')
        return None
    
    def deleteRow(self,spreadsheet_id,sheet_name,row_index):
        """Delete row in Google Drive file

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            sheet_name (str): name of the sheet
            row_index (str): index of the row to delete

        Returns:
            res: information from the sheet_name of the spreadsheet_id
        """
        if not self.service:
            self.connect()

        sheet_id=self.getSheetId(spreadsheet_id,sheet_name)


        #### batchUpdate => Supprimer la ligne mais génère erreur pour les lignes de 8 à 66
        request = self.service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={
                    'requests': [
                        {
                            'deleteRange': {
                                'range': {
                                    'sheetId': sheet_id,
                                    'startRowIndex': row_index - 1,
                                    'endRowIndex': row_index
                                },
                                'shiftDimension': 'ROWS'
                            }
                        }
                    ]
                }
            ).execute()
        return request
    
    #TO DELETE
    def getAllValuesFromSheet(self,spreadsheetId,sheetName,prange):
        res = []
        if not self.service:
            self.connect()
        
        sheetRange = str(sheetName)+'!'+str(prange)
        request = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheetRange)
        response = request.execute()
        if 'values' in response:
            for value in response['values']:
                res.append(value)
           
        return res