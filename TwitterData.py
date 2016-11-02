# -*- coding: utf-8 -*-
"""

COSC - 287
Guy Burstein, Justin Hegyi, Tommy Peele

"""

import codecs
import os
import tweepy
from bs4 import BeautifulSoup

applicationName = "Data_Science_GU"
accessToken = "Your info here"
accessSecret = "Your info here"
consumerKey = "Your info here"
consumerSecret = "Your info here"

print("Connecting to Twitter...")
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth, parser = tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
inputFile = codecs.open("isis.txt", "r", "utf-8")

tweetNum = 0
isisTweeters = set()

print("Reading tweets...")
for line in inputFile:
	tweetNum += 1
	print("Tweet Number: " + str(tweetNum))
	soup = BeautifulSoup(line, "lxml")
	tweet = soup.find("tweet")
	isisTweeters.add(tweet.find("handle").get_text()[1:])
	

print("Retrieving recent tweets...")
with open("NewUserTweets.txt", "wb") as outputFile, open("NewTweeterList.txt", "w") as tweeterFile:
	tweeterCount = len(isisTweeters)
	originalCount = tweeterCount
	for tweeter in isisTweeters:
		print("Remaining Twitter Users: " + str(tweeterCount) + "/" + str(originalCount))
		tweeterCount -= 1
		tweeterFile.write(tweeter + "\n")
		try:
			searchResults = api.user_timeline(screen_name = tweeter)
			for tweet in searchResults:
				output = "<TWEET><TERM>"
				for hashtag in tweet["entities"]["hashtags"]:
					output += "#" + hashtag["text"]
				output += "</TERM>"
				output += "<HANDLE>@" + tweet["user"]["screen_name"] + "</HANDLE>"
				output += "<LOCATION>" + tweet["user"]["location"] + "</LOCATION>"
				output += "<LANGUAGE>" + tweet["user"]["lang"] + "</LANGUAGE>"
				output += "<DEFAULT_IMAGE>" + str(tweet["user"]["default_profile_image"]) + "</DEFAULT_IMAGE>"
				output += "<FOLLOWER_COUNT>" + str(tweet["user"]["followers_count"]) + "</FOLLOWER_COUNT>"
				output += "<FRIEND_COUNT>" + str(tweet["user"]["friends_count"]) + "</FRIEND_COUNT>"
				output += "<STATUS_COUNT>" + str(tweet["user"]["statuses_count"]) + "</STATUS_COUNT>"
				output += "<ID>" + str(tweet["id"]) + "</ID>"
				output += "<TIME>" + tweet["created_at"] + "</TIME>"
				output += "<RETWEET_COUNT>" + str(tweet["retweet_count"]) + "</RETWEET_COUNT>"
				output += "<TEXT>" + tweet["text"] + "</TEXT></TWEET>\n"
				outputFile.write(output.encode("utf8"))
		except tweepy.error.TweepError:
			print("Failed to retrieve data for @" + tweeter + ". Skipping...")
