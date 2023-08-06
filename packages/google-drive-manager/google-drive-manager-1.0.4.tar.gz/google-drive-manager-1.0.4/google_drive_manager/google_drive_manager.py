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
    
    def getSpreadSheetInfoByID(self,spreadsheetID):
        sheet = None
        if not self.service:
            self.connect()
        
        ssheet = self.service.spreadsheets()
        sheet = ssheet.get(spreadsheetId=spreadsheetID).execute()
        return sheet

    def listSheets(self,spreadsheetid):
        if not self.service:
            self.connect()
        sheetMetadata = None
        try:
            sheetMetadata = self.service.spreadsheets().get(spreadsheetId=spreadsheetid).execute()
        except Exception as e:
            print('An error occurred')
            print(e)

        if sheetMetadata != None : 
            sheetMetadata = sheetMetadata.get('sheets', '')
        return sheetMetadata

    def getSheetByName(self,spreadsheetid,name):
        result = False
        if not self.service : 
            self.connect()

        if self.service:
            sheets = self.listSheets(spreadsheetid)    
            for sheet in sheets:
                if sheet['properties']['title'] == name:
                    result = sheet
                    return sheet
        return result

    def getPosDataInCol(self,spreadsheetId,sheetName,prange,search):
        if not self.service:
            self.connect()
        
        sheetRange = str(sheetName)+'!'+str(prange)
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheetRange).execute()
        i = 1
        if 'values' in response:
            for value in response['values']:
                if str(search) in str(value):
                    break
                i=i+1
        return i

    def getRowDataFromSheet(self,spreadsheetId,sheetName,rowNum):
        res = []
        if not self.service:
            self.connect()
        
        sheetRange = str(sheetName)+'!A'+str(rowNum)+':ZZ'+str(rowNum)
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheetRange).execute()
        if 'values' in response:
            for value in response['values']:
                for cell in value:
                    res.append(cell)
        return res

    def getRangeDataFromSheet(self,spreadsheetId,sheetName,pRange):
        if not self.service:
            self.connect()
        
        sheetRange = str(sheetName)+'!'+str(pRange)
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId,range=sheetRange).execute()
        if 'values' in response:
            return response['values']
        return []

    def getColDataFromSheet(self,spreadsheetId,sheetName,colname):
        if not self.service:
            self.connect()
        
        sheetRange = str(sheetName)+'!'+str(colname)+':'+str(colname)
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId,range=sheetRange).execute()
        if 'values' in response:
            return response['values']
        return []

    def getRangeValueFromSheet(self,spreadsheetId,sheetName,prange):
        res = []
        if not self.service:
            self.connect() 
        
        sheetRange = str(sheetName)+'!'+str(prange)
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheetRange).execute()

        if 'values' in response:
            for value in response['values']:
                if len(value) == 1:
                    res.append(str(value[0]))
                if len(value) == 9:
                    res.append({'search':str(value[1]),'label':str(value[0])+' - '+ str(value[1]) + ' - ' + str(value[8])})
        
        return res

    def setColData(self,spreadsheetId,sheetName,colName,colData):
        if not self.service:
            self.connect()
        
        body = {
            "majorDimension": "COLUMNS",
            "values": [colData]
        }
        sheetRange = str(sheetName)+'!'+str(colName)
        
        result = self.service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId, range=sheetRange,
        valueInputOption='RAW',
        body=body).execute()

        return result
    
    def setRangeData(self,spreadsheetId,sheetName,colName,colData):
        if not self.service:
            self.connect()

        body = {
            "majorDimension": "ROWS",
            "values": colData
        }
        sheetRange = str(sheetName)+'!'+str(colName)

        result = self.service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId, range=sheetRange,
        valueInputOption='RAW',
        body=body).execute()

        return result

    def getFileByID(self,folderID):
        self.connect()
        page_token = None
        try:
            service = build('drive', 'v3', credentials= self.creds)
            page_token = None
            # Call the Drive v3 API
            filters = "'{}' in parents".format(folderID)

            while True:
                response = service.files().list(q= f"mimeType='text/csv' and {filters}",
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
                for file in response.get('files', []):
                    # Process change
                    print("Found file: {} ({})".format(file.get('name'), file.get('id')))
                    if file.get('name') == "erp_extract_for_tc.csv":
                        return file.get('id')
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break
        except HTTPError as error:
            print(f'An error occurred: {error}')