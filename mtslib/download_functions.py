from imdb import IMDb
from fuzzywuzzy import fuzz, process
import mtslib.constants as const


def get_imdb_info(sheet):
	ia = IMDb()
	update_range=const.MOVIE_UPDATE_RANGE
	list_of_sheet_records = sheet.get_all_records()
	return_obj_list=[]
	for idx, row in enumerate(list_of_sheet_records):
		if row['Movie']!='':
			print(row['Movie'])
			movie_list = ia.search_movie(str(row['Movie']))
			
			best_movie=process.extractOne(str(row['Movie']), movie_list,score_cutoff = 90)[0]

			best_movie=ia.get_movie(best_movie.movieID)
		
			title=best_movie.get('title','')
			year=best_movie.get('year','')
			cover_url=best_movie.get('cover url','')
			return_obj_list.append([title,
									year,
									cover_url])
	return return_obj_list, update_range

def get_dvd_info():
	pass

def get_vg_info():
	pass

def get_cd_info():
	pass

def get_book_info():
	pass

def get_ebook_info():
	pass

def get_album_info():
	pass