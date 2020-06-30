import mtslib.get_sheets as gts
import mtslib.google_sheets as gs


def get_sheets(doc_name):
	"""Get sheet list from Google Sheets document

	Args:
		doc_name (str): Name of Google Sheets Document

	Returns:
		list:str: List of sheet names
	"""
	#get google sheets client object
	client = gs.get_client()
	doc = client.open(doc_name)
	worksheet_list=doc.worksheets()
	
	return worksheet_list
	