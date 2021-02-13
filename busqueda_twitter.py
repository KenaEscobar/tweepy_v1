# Instalamos la librería
#pip install tweepy
# Importamos la librería
import tweepy
import pandas as pd
from textblob import Texblob
import json
import numpy as np 
import nltk

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
api = tweepy.API(auth)

clave_busqueda = "mapuche"
cantidad = 10

search_twetter = [status for status in tweepy.Cursor(api.search, q = clave_busqueda).items(cantidad)]

print (search_twetter)


"""
resultado = api.search( q = clave_busqueda, tweet_mode='extended', result_type='recent')[0]
print(resultado)
print (type (resultado))
f = open('twitter.txt', 'a', encoding = 'utf-8')
f.write(str(resultado))
f.close()
"""

#Analisis de datos obtenidos 
positivos = 0
negativos = 0
neutros = 0

for tweet in search_twetter:
    analysis = Texblob(tweet.text)
    if analysis.sen