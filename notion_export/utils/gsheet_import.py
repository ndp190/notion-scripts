import gspread
from google.oauth2.service_account import Credentials

def import_sprint_tasks(sprint_tasks, google_sheet_key, google_sheet_index):
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(
        'client_secrets.json', scopes=scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key(google_sheet_key)
    worksheet = wks.get_worksheet(int(google_sheet_index))
    
    if worksheet.row_values(1) == []:
        worksheet.append_row(
            ['id', 'title', 'app', 'epic', 'sprint', 'status', 'point', 'import_time'])
    
    worksheet.append_rows(sprint_tasks)
