#import csv
from bs4 import BeautifulSoup

inputFile1 = open("NewUserTweets.txt", "r")
outputFile1 = open("NewUserTweets.csv", "w")

#outputWriter = csv.writer(outputFile, delimiter = "|")
#outputWriter.writerow(["Term|Handle"])#Location|Language|Default Image|Follower Count|Friend Count|Status Count|ID|Time|Retweet Count|Text\n"])

outputFile1.write("Term,Handle,Location,Language,Default Image,Follower Count,Friend Count,Status Count,ID,Time,Retweet Count,Text\n")

tweetCount = 0
for line in inputFile1:
    soup = BeautifulSoup(line, "lxml")
    tweet = soup.find_all("tweet")
    tweetCount += 1
    if tweetCount != 69 & tweetCount != 504 & tweetCount != 498 & tweetCount != 494 & tweetCount != 894 & tweetCount != 822: #Problematic tweet indices
        try:
            term = tweet[0].find_all("term")[0].get_text()
            handle = tweet[0].find_all("handle")[0].get_text()
            location = tweet[0].find_all("location")[0].get_text()
            language = tweet[0].find_all("language")[0].get_text()
            default_image = tweet[0].find_all("default_image")[0].get_text()
            follower_count = tweet[0].find_all("follower_count")[0].get_text()
            friend_count = tweet[0].find_all("friend_count")[0].get_text()
            status_count = tweet[0].find_all("status_count")[0].get_text()
            id = tweet[0].find_all("id")[0].get_text()
            time = tweet[0].find_all("time")[0].get_text()
            retweet_count = tweet[0].find_all("retweet_count")[0].get_text()
            text = tweet[0].find_all("text")[0].get_text()
            output = "\"" + term + "\",\"" + handle + "\",\"" + location + "\",\"" + language + "\",\"" + default_image + "\",\"" + follower_count + "\",\"" + friend_count + "\",\"" + status_count + "\",\"" + id + "\",\"" + time + "\",\"" + retweet_count + "\",\"" + text + "\"\n"
            outputFile1.write(output)
        except IndexError:
            "Error with line..."

inputFile1.close()
outputFile1.close()

inputFile2 = open("isis_sample.txt", "r")
outputFile2 = open("isis_sample.csv", "w")

outputFile2.write("Term,Handle,Location,Language,Default Image,Follower Count,Friend Count,Status Count,ID,Time,Retweet Count,Text\n")
tweetCount = 0
for line in inputFile2:
    soup = BeautifulSoup(line, "lxml")
    tweet = soup.find_all("tweet")
    tweetCount += 1
    try:
        term = tweet[0].find_all("term")[0].get_text()
        handle = tweet[0].find_all("handle")[0].get_text()
        location = tweet[0].find_all("location")[0].get_text()
        language = tweet[0].find_all("language")[0].get_text()
        default_image = tweet[0].find_all("default_image")[0].get_text()
        follower_count = tweet[0].find_all("follower_count")[0].get_text()
        friend_count = tweet[0].find_all("friend_count")[0].get_text()
        status_count = tweet[0].find_all("status_count")[0].get_text()
        id = tweet[0].find_all("id")[0].get_text()
        time = tweet[0].find_all("time")[0].get_text()
        retweet_count = tweet[0].find_all("retweet_count")[0].get_text()
        text = tweet[0].find_all("text")[0].get_text()
        output = "\"" + term + "\",\"" + handle + "\",\"" + location + "\",\"" + language + "\",\"" + default_image + "\",\"" + follower_count + "\",\"" + friend_count + "\",\"" + status_count + "\",\"" + id + "\",\"" + time + "\",\"" + retweet_count + "\",\"" + text + "\"\n"
        outputFile2.write(output)
    except IndexError:
        "Error with line..."