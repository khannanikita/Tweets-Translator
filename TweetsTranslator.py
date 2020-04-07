import googletrans

print(googletrans.LANGUAGES)
from googletrans import Translator

text1 = '''
A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott 
államalakulat volt a Földközi-tenger medencéjében
'''

text2 = '''
Vysoké Tatry sú najvyššie pohorie na Slovensku a v Poľsku a sú zároveň jediným 
horstvom v týchto štátoch s alpským charakterom. 
'''

translator = Translator()

dt1 = translator.detect(text1)
print(dt1)

dt2 = translator.detect(text2)
print(dt2)
translated = translator.translate('आपला दिवस कसा आहे?')

print(translated.text)



translated = translator.translate('आपला दिवस कसा आहे?', dest='urdu')
print(translated.text)

   
import pandas as pd
import numpy as np

consumer_key = 'a1aF19OS7Cop3B6dbBliIZDiM'
consumer_secret = 'yVJhkSHN9cyJHB44mRK5SFiAZzLaCj7GbMQt1aqlTBiziqwfZL'
access_token = '1180015877938278400-UocdoXpQZD59O0n9dKsJS3iAqjCawL'
access_token_secret = 'jKFsWrcL7ELUoBThe9hTywZOJD1udo0O4bIditJnhSSU2'
import tweepy
from textblob import TextBlob
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print(api.me())
api = tweepy.API(auth)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
search_words = '#यूपी_के_मन_का_बजट'
date_since = "2020-02-18"
tweets = tweepy.Cursor(api.search,
              q=search_words,
              since=date_since).items(5)

for tweet in tweets:
    print(tweet.text)
    print("Translating to English")
    translated = translator.translate(tweet.text)
    print(translated.text)