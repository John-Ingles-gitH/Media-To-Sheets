from oauth2client.service_account import ServiceAccountCredentials
import gspread
import mtslib.constants as const

def get_client():
	"""Connects to Google Sheets using the secret key and returns the client

	Returns:
		<class 'gspread.client.Client'>: Manipulate a google sheets document
	"""
	scope = [const.GOOGLESHEETS_SCOPE, const.GOOGLEDRIVE_SCOPE]

	credentials = ServiceAccountCredentials.from_json_keyfile_name('mtslib/'+ const.SECRET, scope)

	return gspread.authorize(credentials)


