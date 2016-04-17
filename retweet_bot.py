import tweepy
import time

'''
To obtain consumer_key, consumer_secret, access_token, access_token_secret
Go to https://apps.twitter.com/
Sign in, follow the instructions for creating new application
Above codes are listed under "Keys and Access Tokens"
May have to "generate consumer key and secret" (there's a button)

Also, enter desired twitter handle below
'''

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

minute = -1 # Will make sure the first iteration triggers else loop below
while True:
    if(minute == time.strftime("%M")):
        time.sleep(30)
    else:
        minute = time.strftime("%M")
        print(time.strftime("%I:%M"))
        for tweet in api.user_timeline('twitter_handle'): # Enter twitter handle here
            try:
                api.retweet(tweet.id)
                print("Retweeted")
            except Exception as e: # If tweet is already retweeted, will print error
                print(e)
            try:
                api.create_favorite(tweet.id)
                print("Favorited")
            except Exception as e: # If tweet is already favorited, will print error
                print(e)
