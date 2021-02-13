# Instalamos la librería
#pip install tweepy
# Importamos la librería
import tweepy
import pandas as pd
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
#resultado = api.search(q='Mapuche')[0].text

resultado = api.search(q='mapuche constituyente', tweet_mode='extended', result_type='recent')[0]
print(resultado)
print (type (resultado))
f = open('twitter.txt', 'a', encoding = 'utf-8')
f.write(str(resultado))
f.close()


