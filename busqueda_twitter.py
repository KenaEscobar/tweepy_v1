import tweepy
import pandas as pd
#from textblob import TextBlob
import json
import numpy as np 
import matplotlib.pyplot as plt
import re
from io import StringIO

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
api = tweepy.API(auth, wait_on_rate_limit= True ,wait_on_rate_limit_notify= True)

clave_busqueda = "mapuche constituyente"
cantidad = 500
search_twetter = [status for status in tweepy.Cursor(api.search, q = "mapuche", tweet_mode='extended').items(cantidad)]


#Creación de DataFrame

my_list_of_dicts = []
for each_json in search_twetter:
    if each_json.full_text.startswith('RT'):
        continue
    my_list_of_dicts.append(each_json._json)

with open('twetter_json_Data.txt', 'w' ) as file :
    file.write(json.dumps(my_list_of_dicts,indent=4))

my_demo_list = []
with open('twetter_json_Data.txt', encoding= 'utf-8') as json_file:
    all_data = json.load (json_file)
    for each_diccionary in all_data:
    
        #print(each_diccionary)

        created_at = each_diccionary ['created_at']
        tweet_id = each_diccionary ['id']
        full_text = each_diccionary['full_text']

    #formila trae todo lo que está en user. No filtra el dato especifico que se requiere.
        screen_name = each_diccionary['user'],['screen_name']
        name = each_diccionary ['user'],['name']
        location = each_diccionary ['user'],['location']

        followers_count = each_diccionary ['user'],['followers_count']
        friends_count = each_diccionary ['user'],['friends_count']
        retweet_count = each_diccionary ['user'],['retweet_count']
      

        my_demo_list.append ({
            'tweet_id':str (tweet_id),
        'full_text':str (full_text),
        'screen_name':str (screen_name),
        'name':str (name),
        'location':str (location),
        'followers_count': str (followers_count), 
        'friends_count': str (friends_count), 
        'retweet_count': str (retweet_count),
        'created_at': created_at,})

        twette_dataset = pd.DataFrame (my_demo_list, columns = ['tweet_id' , 'full_text','screen_name',
        'name','location','followers_count','friends_count', 'retwett_count' , 'create_count'])
        # Escribir para futuras referencias a scv 
        twette_dataset.to_csv('twetter_data.csv')      





