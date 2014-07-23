import sys
import json
import string
from collections import defaultdict


""""
Problen 2: Derive the sentiment of each tweet
accepts two arguments on the command line: a sentiment file 
and a tweet file.
Ex: $ python tweet_sentiment.py AFINN-111.txt output.txt

 file AFINN-111.txt contains a list of pre-computed sentiment scores. 
 Each line in the file contains a word or phrase followed by a sentiment score. 
 Each word or phrase that is found in a tweet but not found in AFINN-111.txt 
 should be given a sentiment score of 0. See the file AFINN-README.txt for more information.

Tweets Field Guide: https://dev.twitter.com/docs/platform-objects/tweets
Python Dict: https://docs.python.org/2/library/stdtypes.html#typesmapping


"""


def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	lines(sent_file)
	lines(tweet_file)

def eng_tweets(tweets_all, key, valuelist):

	return [engtweets for engtweets in tweets_all if engtweets[key] in valuelist]


def us_tweets(list, key, valuelist):
	return [ ustweets for ustweets in tweets_all if ustweets[key]in valuelist]


def cleanup(raw_text):
    cleaned_up = ""
    for char in raw_text:
       if char not in punctuations:
           cleaned_up = cleaned_up + char
    return cleaned_up

def sent_score(w):

	for key, val in scores.items():

  		if w == key:
  			tweet_dictionary[w] = val
  			global sum_score
  			sum_score += tweet_dictionary[w] 
  
			
  		else: 
  			scores[w] =0
  			sum_score = sum_score
 

if __name__ == '__main__':

	print "Running sentiment analysis on tweets..."
	main()

	punctuations = set(string.punctuation)

	sent_file = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
  	#print scores.items()

    #tweets =[rec['text'] for rec in tweets_full if 'text' in rec]
	
  	tweets_full= [json.loads(line) for line in open(sys.argv[2])]
	#print tweets_full[0]
	tweets_all = [rec for rec in tweets_full if 'text' and 'lang' and 'place' in rec]
	place_all = [loc for loc in tweets_full if 'place' and 'name' in loc]
	engtweets = eng_tweets(tweets_all, "lang", "en")
	# us_engtweets = us_tweets(tweets_all,"country","United States")

	#tweets =[eng['lang'] for eng in tweets if 'lang' in eng] #checking languages of all english tweets.

	print 'Number of English Tweets: ', len(engtweets)

	place = [l['place']for l in engtweets]

	tweets = [t['text'] for t in engtweets]


	tweet_dictionary={}
	
	For each tweet, print index, content of tweet, parse out content, calculate sent score
	for idx_t, val in enumerate(tweets):
		unicode_string = tweets[idx_t]
		encoded_string = unicode_string.encode('utf-8')
		#print 'upper:', encoded_string
		encoded_string = encoded_string.lower()
		#print 'lower:', encoded_string
		encoded_string = cleanup(encoded_string)

		d = defaultdict(list)

		splt_tweet = encoded_string.split()
		# Initialize sum to be 0 for every tweet.
		print idx_t, encoded_string
		sum_score = 0
		
		for idx_w, val in enumerate(splt_tweet):
			words = splt_tweet[idx_w]

			# Matching words to Sentiment Scores in AFINN-111.txt
			sent_score(words)

		if sum_score != 0:
			print 'sum_score =', sum_score
		else:
			print 'no word match, sum_score = ', sum_score

