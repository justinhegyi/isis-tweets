"""
Justin Hegyi
"""
import os
import codecs
from bs4 import BeautifulSoup

def generateSet(filePath):
	with open(filePath, 'r') as allTerms:
		toReturn = set()
		for term in allTerms:
			toReturn.add(term.strip().lower())
	
	return toReturn

politicalWordSet = generateSet("PoliticalWordList.txt")

totalScore = 0.0

lineCount = 0
with codecs.open("AllRedditSubmissions.txt", "r", "utf-8") as inputFile, codecs.open("ProcessedSubmissions.txt", "w", "utf-8") as outputFile:
	for line in inputFile:
		politicalWordPercent = 0.0
		lineCount += 1
		soup = BeautifulSoup(line, "lxml")
		comment = soup.find_all("submission")

		try:
			for text in comment:
				textToParse = text.find_all("text")[0].get_text()
				titles = text.find_all("title")[0].get_text()
			lineCount += 1
			splitTextArray = textToParse.split()
			splitTextArray.extend(titles.split())
			wordCount = 0
			politicalWordCount = 0
			for word in splitTextArray:
				wordCount += 1
				toCompare = word.lower()
				if (toCompare in politicalWordSet):
					politicalWordCount += 1


			
			if wordCount == 0:
				#this ensures that any comment without text will be recorded with a plistscore of 0
				wordCount = 1
			politicalWordPercent = politicalWordCount / wordCount
			totalScore += politicalWordPercent
			
			if politicalWordPercent != 0.0:
				outputFile.write(str(comment[0])[:-8] + "<plistscore>" + str(politicalWordPercent) + "</plistscore></comment>\n")
		except IndexError:
			"Error with line..."

			
averageScore = totalScore / lineCount

print("Average score for political word: " + str(averageScore))