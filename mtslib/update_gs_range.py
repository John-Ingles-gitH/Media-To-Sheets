def update_gs_range(vals, sheet, cell_range):
	"""Update range of cells in a google sheets sheet

	Args:
		vals (list:list:str): List of lists of movie attributes [[title,year,cover_url],...]
		sheet (<class Sheet>): Google Sheets sheet object
		cell_range (str): cell range in [A-Z][int]:[A-Z][int] style
	"""
	sheet.spreadsheet.values_update(
    f'{sheet.title}!{cell_range}', 
    params={'valueInputOption': 'RAW'}, 
    body={'values': vals})