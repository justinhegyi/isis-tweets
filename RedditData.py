# -*- coding: utf-8 -*-
"""

COSC - 287
Guy Burstein, Justin Hegyi, Tommy Peele

"""

import praw
import os
import datetime

user_agent = "Data Science Project - GU"
reddit = praw.Reddit(user_agent = user_agent)

if (os.path.exists("AllRedditSubmissions.txt")):
	os.remove("AllRedditSubmissions.txt")
if (os.path.exists("AllRedditComments.txt")):
	os.remove("AllRedditComments.txt")
	
with open("NewTweeterList.txt", "r") as userList, open("AllRedditSubmissions.txt", "w") as submissionsOutput, open("AllRedditComments.txt", "w") as commentsOutput:
	retrievedData = 1
	for username in userList:
		print("Retrieving data for user " + str(retrievedData) + "/524717")
		retrievedData += 1
		user = reddit.get_redditor(username)
		userSubmitted = user.get_submitted()
		userCommented = user.get_comments()
		try:
			for post in userSubmitted:
				submissionText = "<SUBMISSION><USERNAME>" + username.strip() + "</USERNAME>"
				submissionText += "<POSTID>" + post.id + "</POSTID>"
				submissionText += "<TIME>" + str(datetime.datetime.fromtimestamp(post.created)) + "</TIME>"
				submissionText += "<TITLE>" + post.title + "</TITLE>"
				submissionText += "<SUBREDDIT>" + post.subreddit.display_name + "</SUBREDDIT>"
				submissionText += "<SCORE>" + str(post.score) + "</SCORE>"
				submissionText += "<NUM_COMMENTS>" + str(post.num_comments) + "</NUM_COMMENTS>"
				submissionText += "<TEXT>" + post.selftext + "</TEXT></SUBMISSION>\n"
				
				submissionsOutput.write(submissionText)
		except praw.errors.NotFound:
			print(username + " has no submissions.")
			
		try:
			for comment in userCommented:
				commentText = "<COMMENT><USERNAME>" + username.strip() + "</USERNAME>"
				commentText += "<POSTID>" + comment.id + "</POSTID>"
				commentText += "<TIME>" + str(datetime.datetime.fromtimestamp(comment.created)) + "</TIME>"
				commentText += "<SUBREDDIT>" + comment.subreddit.display_name + "</SUBREDDIT>"
				commentText += "<SCORE>" + str(comment.score) + "</SCORE>"
				commentText += "<GOLD>" + str(comment.gilded) + "</GOLD>"
				commentText += "<TEXT>" + comment.body + "</TEXT></COMMENT>\n"
				
				commentsOutput.write(commentText)
		except praw.errors.NotFound:
			print(username + " has no comments.")