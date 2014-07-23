import sys
import json
import string
from collections import defaultdict



"""
Part 4:
a script compute the term frequency histogram of the livestream data you harvested from Problem 1.

The frequency of a term can be calculated as 
[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
"""

def lines(fp):
	print str(len(fp.readlines()))

def main():
	
	tweet_file = open(sys.argv[1])
	#lines(tweet_file)

def eng_tweets(tweets_all, key, valuelist):
	return [engtweets for engtweets in tweets_all if engtweets[key] in valuelist]

def cleanup(raw_text):
    cleaned_up = ""
    for char in raw_text:
       if char not in punctuations:
           cleaned_up = cleaned_up + char
    return cleaned_up


def count(w):
  	term_dict[w] += 1
  	return term_dict


if __name__ == '__main__':

	#print "Running sentiment analysis on tweets..."
	main()

	
	#The set of punctuation in the string module
	punctuations = set(string.punctuation)
  	tweets_full= [json.loads(line) for line in open(sys.argv[1])]

	tweets_all = [rec for rec in tweets_full if 'text' and 'lang' in rec]
	engtweets = eng_tweets(tweets_all, "lang", "en")
	#tweets =[eng['lang'] for eng in tweets if 'lang' in eng] #checking languages of all english tweets.

	
	tweets = [t['text'] for t in engtweets]

	term_dict = {}
	terms =[]
	all_term = 0
	

	# For each tweet, print index, content of tweet, parse out content, calculate sent score
	for idx_t, val_t in enumerate(tweets):
		unicode_string = tweets[idx_t]
		#print 'upper:', encoded_string
		encoded_string = unicode_string.encode('utf-8')
		#print 'lower:', encoded_string
		encoded_string = encoded_string.lower()
		
	
		encoded_string = cleanup(encoded_string)

		splt_tweet = encoded_string.split()
	
		for idx_w, val_w in enumerate(splt_tweet):
			word = splt_tweet[idx_w]
			terms.append(word)		

		for val_n in terms:
			all_term += 1

			# Add a new term to term_dict if it doesn't exist yet
			if val_n not in term_dict: 
				term_dict[val_n] = 1
				
			
			else:
				term_dict[val_n] += 1
	
		#print list(set(splt_tweet))
	#print all_term
	
	for key, val in term_dict.items():
		if len(key) == 0:
			continue

		# [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
		freq = float(val)/float(all_term)
		print key, ("%.4f" %freq )		
		#print type(key), type(freq)
	
	
	
	





		



















