import pandas as pd
import requests,time
import json,re,os
from csv import writer
from urllib.error import HTTPError
from googletrans import Translator
translator = Translator()

source_lan = "en"
translated_to= "si"

data = pd.read_csv('./data/file.csv')

data.to_json(path_or_buf='artists.json',orient='records',lines=False)

word = translator.translate("old")

translated_text = translator.translate("old", src=source_lan, dest = translated_to)

with open('file.csv', 'w', encoding='utf8') as f:
    thewriter = writer(f)
    thewriter.writerow(translated_text)


def translate_field(field_array,field_all_dict):
	if field_array:
		translated_field_array = []
		if type(field_array) == list:
			for eng_data in field_array:
				eng_data = eng_data.strip()
				if eng_data in field_all_dict:
					sin_data = field_all_dict[eng_data]
				else:
					try:
						sin_tran_data = translator.translate(eng_data, src='en', dest='si')
						sin_data = sin_tran_data.text
					except HTTPError:
						time.sleep(5)
					try:
						sin_tran_data = translator.translate(eng_data, src='en', dest='si')
						sin_data = sin_tran_data.text
					except HTTPError:
						print("error")
					field_all_dict.update({eng_data: sin_data})
				translated_field_array.append(sin_data)
			return translated_field_array, field_all_dict
		else:
			eng_data = field_array.strip()
			if eng_data in field_all_dict:
				sin_data = field_all_dict[eng_data]
			else:
				try:
					sin_tran_data = translator.translate(eng_data, src='en', dest='si')
					sin_data = sin_tran_data.text
				except HTTPError:
					time.sleep(5)
				try:
					sin_tran_data = translator.translate(eng_data, src='en', dest='si')
					sin_data = sin_tran_data.text
				except HTTPError:
					print("error") 
				field_all_dict.update({eng_data: sin_data})
			translated_field_array.append(sin_data)
			return translated_field_array[0], field_all_dict
	else:
		return None,field_all_dict

def translate():
    artist_dict = {}
    country_dict = {}
    songs_dict = {}

	with open('translated_artists.json', 'r',encoding='utf8') as s_file:
		final_data = json.loads(s_file.read())
    
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	artists_file = os.path.join(THIS_FOLDER, 'my.json')

	with open(artists_file, 'r', encoding='utf8') as f:
		artists = json.loads(f.read())
    # artists  = open(artist_file,encoding='utf8')

    
	i=0
	for artist in artists:
		i=i+1
		if(i%10==0):
			time.sleep(15)        
        
        complete_data = {}
		artist_name = artist['artist_name']
        country = artist['country']
        songs = artist['songs']
		
		translated_artist_name, artist_dict = translate_field(artist_name, artist_dict)
		time.sleep(2)
        
        translated_country, country_dict = translate_field(country, country_dict)
		time.sleep(2)

        translated_songs, songs_dict = translate_field(songs, songs_dict)
		time.sleep(2)

		complete_data = {
            "sinhala_artist_name": translated_artist_name,
            "english_artist_name": artist_name,
            "sinhala_country": translated_country,
            "english_country": country,
            "sinhala_songs": translated_songs,
            "english_songs": songs,
        }        

		final_data.append(complete_data)
		with open('translated_artists.json', 'w', encoding='utf8') as tra_songs:
			json.dump(final_data,tra_songs, indent=4 ,ensure_ascii=False)
			
        
		print(songs_dict)

if __name__ == "__main__":
	translate()
