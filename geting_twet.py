from tweepy import Cursor
from twetter_client import get_twetter_client


if __name__=='__main__':
    client = get_twetter_client()

    for status in Cursor(client.home_timeline).items (10):
        #procesa a single status
        print (status.text)






