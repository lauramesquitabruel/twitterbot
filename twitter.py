import tweepy 

api_key = ""
api_secret = ""
bearer_token = ""
acess_token = ""
acess_secret = ""

client = tweepy.Client(bearer_token, api_key, api_secret, acess_token, acess_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, acess_token, acess_secret)
api = tweepy.API(auth)

client.create_tweet(text = "")

client.like("")

client.retweet("")

client.create_tweet(in_reply_to_tweet_id="", text = "")
