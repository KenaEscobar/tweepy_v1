import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twetter_auth():
    """Setup twetter authentication. 
    Return: twetter.OauthHandler object"""

    try: 
        consumer_key = os.environ['zRMVMOe2p0yA26cT5e8thrFsZ']
        consumer_secret = os.environ['ags6DBFrvBsyuno2xcxONBhchNO2TcZrUvr5XITZA7hwf5OB80']
        access_token = os.environ['1356210137954983939-aNGnviNvx8XIVSIJMzvaEOkeoGhXhl' ]
        access_secret = os.environ['82ypQXaaMcp3kH6JCi8v8T7XQpRjQt8zdUpiXg35XmNc0']
    except KeyError: 
        sys.stderr.write:("TWETTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler (consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twetter_client():
    """ Setup Twetter Client API 
    Return: twetter.api object """

    auth = get_twetter_auth()
    client = API (auth)
    return client
 








