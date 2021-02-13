print('Primera prueba de entrada')
import json
from tweepy import Cursor
from twetter_client import get_twetter_client

if __name__ == '__main__':

    clien = get_twetter_client()
    with open('home_timeline.jsonl', 'w') as f:
        for pages in Cursor (clien.home_timeline,count=200).pages(4):
            for status in pages:
                f.write(json.dumps(status._json)+"\n") 
                print(get_twetter_client) 

                      