import numpy as np
import pandas as pd
from pprint import pprint

dataFrame = pd.read_csv("NewUserTweets.csv", sep = ",", encoding = "latin1")
print("NewUserTweets.csv Cleanliness Evaluation")

validTerms = dataFrame[dataFrame["Term"].notnull()]
print("Number of tweets with missing Term values:", len(dataFrame) - len(validTerms))

validHandles = dataFrame[dataFrame["Handle"].notnull()]
print("Number of tweets with missing Handle values:", len(dataFrame) - len(validHandles))

validLocations = dataFrame[dataFrame["Location"].notnull()]
print("Number of tweets with missing Location values:", len(dataFrame) - len(validLocations))

validLanguages = dataFrame[dataFrame["Language"].notnull()]
print("Number of tweets with missing Language values:", len(dataFrame) - len(validLanguages))

validDefaultImages = dataFrame[dataFrame["Default Image"].notnull()]
print("Number of tweets with missing Default Image values:", len(dataFrame) - len(validDefaultImages))

validFollowerCount = dataFrame[dataFrame["Follower Count"].notnull()]
print("Number of tweets with missing Follower Count values:", len(dataFrame) - len(validFollowerCount))

validFriendCount = dataFrame[dataFrame["Friend Count"].notnull()]
print("Number of tweets with missing Friend Count values:", len(dataFrame) - len(validFriendCount))

validStatusCounts = dataFrame[dataFrame["Status Count"].notnull()]
print("Number of tweets with missing Status Count values:", len(dataFrame) - len(validStatusCounts))

validIDs = dataFrame[dataFrame["ID"].notnull()]
print("Number of tweets with missing ID values:", len(dataFrame) - len(validIDs))

validTimes = dataFrame[dataFrame["Time"].notnull()]
print("Number of tweets with missing Time values:", len(dataFrame) - len(validTimes))

validRetweetCounts = dataFrame[dataFrame["Retweet Count"].notnull()]
print("Number of tweets with missing Retweet Count values:", len(dataFrame) - len(validRetweetCounts))

validTexts = dataFrame[dataFrame["Text"].notnull()]
print("Number of tweets with missing Text values:", len(dataFrame) - len(validTexts))

dataFrame = pd.read_csv("isis_sample.csv", sep = ",", encoding = "latin1")
print("isis_sample.csv Cleanliness Evaluation")

validTerms = dataFrame[dataFrame["Term"].notnull()]
print("Number of tweets with missing Term values:", len(dataFrame) - len(validTerms))

validHandles = dataFrame[dataFrame["Handle"].notnull()]
print("Number of tweets with missing Handle values:", len(dataFrame) - len(validHandles))

validLocations = dataFrame[dataFrame["Location"].notnull()]
print("Number of tweets with missing Location values:", len(dataFrame) - len(validLocations))

validLanguages = dataFrame[dataFrame["Language"].notnull()]
print("Number of tweets with missing Language values:", len(dataFrame) - len(validLanguages))

validDefaultImages = dataFrame[dataFrame["Default Image"].notnull()]
print("Number of tweets with missing Default Image values:", len(dataFrame) - len(validDefaultImages))

validFollowerCount = dataFrame[dataFrame["Follower Count"].notnull()]
print("Number of tweets with missing Follower Count values:", len(dataFrame) - len(validFollowerCount))

validFriendCount = dataFrame[dataFrame["Friend Count"].notnull()]
print("Number of tweets with missing Friend Count values:", len(dataFrame) - len(validFriendCount))

validStatusCounts = dataFrame[dataFrame["Status Count"].notnull()]
print("Number of tweets with missing Status Count values:", len(dataFrame) - len(validStatusCounts))

validIDs = dataFrame[dataFrame["ID"].notnull()]
print("Number of tweets with missing ID values:", len(dataFrame) - len(validIDs))

validTimes = dataFrame[dataFrame["Time"].notnull()]
print("Number of tweets with missing Time values:", len(dataFrame) - len(validTimes))

validRetweetCounts = dataFrame[dataFrame["Retweet Count"].notnull()]
print("Number of tweets with missing Retweet Count values:", len(dataFrame) - len(validRetweetCounts))

validTexts = dataFrame[dataFrame["Text"].notnull()]
print("Number of tweets with missing Text values:", len(dataFrame) - len(validTexts))