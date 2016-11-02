import os
import tweepy
import codecs
from bs4 import BeautifulSoup

def generateSet(filePath):
	with open(filePath, 'r') as allTerms:
		toReturn = set()
		for term in allTerms:
			toReturn.add(term.strip().lower())
	
	return toReturn

set1 = generateSet("WordList1.txt")
set2 = generateSet("WordList2.txt")

totalScore1 = 0.0
totalScore2 = 0.0

lineCount = 0
with codecs.open("NewUserTweets.txt", "r", "utf-8") as inputFile, codecs.open("ProcessedTweets.txt", "w", "utf-8") as outputFile:
	for line in inputFile:
		lineCount += 1
		soup = BeautifulSoup(line, "lxml")
		tweet = soup.find_all("tweet")
		try:
			textToParse = tweet[0].find_all("text")[0].get_text()
			
			lineCount += 1
			splitTextArray = textToParse.split()
			wordCount = 0
			wordCount1 = 0
			wordCount2 = 0
			for word in splitTextArray:
				wordCount += 1
				toCompare = word.lower()
				if (toCompare in set1):
					wordCount1 += 1
				if (toCompare in set2):
					wordCount2 += 1
			
			wordPercent1 = wordCount1 / wordCount
			totalScore1 += wordPercent1
			wordPercent2 = wordCount2 / wordCount
			totalScore2 += wordPercent2
			
			outputFile.write(str(tweet)[1:-9] + "<l1score>" + str(wordPercent1) + "</l1score><l2score>" + str(wordPercent2) + "</l2score></tweet>\n")
		except IndexError:
			"Error with line..."

			
averageScore1 = totalScore1 / lineCount
averageScore2 = totalScore2 / lineCount

print("Average score for word 1: " + str(averageScore1))
print("Average score for word 2: " + str(averageScore2))
