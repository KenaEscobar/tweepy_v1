# Instalamos la librería
#pip install tweepy
# Importamos la librería
import tweepy
import pandas as pd
from textblob import TextBlob
import json
import numpy as np 
import matplotlib.pyplot as plt
import re
import time
#import nlkt
#nlkt.downloads ('stopwords')
#from nltk.corpus import stopwords
#from nlkt.stem.porter import PorterStemmer
#from wordcloud import WordCloud
#from collections import Counter

# Pasamos los tokens de cliente
consumer_key = "SFPCBPyTxra10ftDpA9ekrPOW"
consumer_secret = "EjBJ1aEChnA0xuXrS3NzxbAELqPuSbRTluWQ8BmgLoB8SQYI2r"
# Si queremos usar OAuth 1.0
access_token = "1356210137954983939-Vnx1iN7nkBl3NYciWgPg7d7Ty5gMuV"
access_token_secret = "C8fCjTyKyCgwY5LIzOtgQDa7D3St7AjLLUYQtwEaDgOSK"

# Creamos un handler con las 2 claves de cliente
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Pasamos los tokens de acceso
auth.set_access_token(access_token, access_token_secret)
# Guardamos la autorizacion a la API en una variable
api = tweepy.API(auth)

#Busqueda usando search
#api = tweepy.API(auth)

clave_busqueda = "mapuche constituyente"
cantidad = 100
time.sleep(3) #este time sleep debe quedar dentro de un for que además me elimine los rt 
search_twetter = [status for status in tweepy.Cursor(api.search, q = clave_busqueda).items(cantidad)]

strlist = str(search_twetter)
json_list = json.dumps(strlist, indent= 4)
print(json_list)

#print(search_twetter)
"""
resultado = api.search( q = clave_busqueda, tweet_mode='extended', result_type='recent')[0]
print(resultado)
print (type (resultado))
f = open('twitter.txt', 'a', encoding = 'utf-8')
f.write(str(resultado))
f.close()
"""
#Analisis de datos obtenidos NLKT
positivos = 0
negativos = 0
neutros = 0

"""for tweet in search_twetter:
    analysis = Textblob(tweet.text)
    if analysis.sentiment [0] > 0:
        positivos = positivos +1
    elif analysis.sentiment [0] > 0:
        negativos = negativos +1
    else:
        neutros = neutros +1

print('Total Positivos ' , positivos)
print('Total Negativos ' , negativos)
print('Total Neutrales ' , neutros)

#Plotting sentiments
labels = 'Positive', 'Negative', 'Neutral'
sizes = [257, 223, 520]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1ª slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()"""

#Creación de DataFrame
my_list_of_dicts = []
for each_json in search_twetter:
    my_list_of_dicts.append(each_json._json)

with open('twetter_json_Data.txt', 'w' ) as file :
    file.write(json.dumps(my_list_of_dicts,indent=4))

my_demo_list = []
with open('twetter_json_Data.txt', encoding= 'utf-8') as json_file:
    all_data = json.load (json_file)
    for each_diccionary in all_data:

        tweet_id = each_diccionary ['id']
        text = each_diccionary['text']
        favorite_count = each_diccionary ['favorite_count']
        retweet_count = each_diccionary ['retweet_count']
        created_at = each_diccionary ['created_at']

        my_demo_list.append ({'tweet_id': str (tweet_id),'text':str (text),
         'favorite_count': int (favorite_count), 'retweet_count': int (retweet_count),
         'created_at': created_at,})

        twette_dataset = pd.DataFrame (my_demo_list, columns = ['tweet_id' , 'text',
        'favorite_count', 'retwett_count' , 'create_count'])
        # Escribir para futuras referencias a scv 
        twette_dataset.to_csv('twetter_data.csv')        





