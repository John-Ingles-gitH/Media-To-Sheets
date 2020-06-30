import mtslib.get_sheets as gts
import mtslib.constants as const
from pick import pick
import mtslib.clear_console as cs
import mtslib.download_functions as df
import mtslib.update_gs_range as ugr

#associate sheets names with actions to perform
download_functions={'Movie Cover via Python':df.get_imdb_info,
				   'DVDs':df.get_dvd_info,
				   'Video Games': df.get_vg_info,
				   'CDs':df.get_cd_info,
				   'Books':df.get_book_info,
				   'eBooks':df.get_ebook_info,
				   'Albums with tracks':df.get_album_info}

def main():
	# Pass a Google Sheets document name and return its sheets
	worksheet_list=gts.get_sheets(const.DOC_NAME)

	#Pick a sheet to process and clear the console
	worksheet_dict={sheet.title:sheet for sheet in worksheet_list}
	current_sheet_title, _ = pick([*worksheet_dict.keys()],"Pick a Sheet")
	current_sheet_object = worksheet_dict[current_sheet_title]
	cs.clear()

	#call 'get' function associated with current sheet and return list of media attributes
	media_attributes, update_range=download_functions[current_sheet_title](current_sheet_object)

	#update current sheet with returned media attributes
	ugr.update_gs_range(media_attributes, current_sheet_object, update_range)