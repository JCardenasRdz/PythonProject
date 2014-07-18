import sys
import json
import string
from collections import defaultdict


"""
Part 3:
a script that computes the sentiment for the terms that do not appear in the file 
AFINN-111.txt.

Here's how you might think about the problem: We know we can use the sentiment-carrying 
words in AFINN-111.txt to deduce the overall sentiment of a tweet. Once you deduce the sentiment 
of a tweet, you can work backwards to deduce the sentiment of the non-sentiment carrying words that do not 
appear in AFINN-111.txt. For example, if the word soccer always appears in proximity with positive words like 
great and fun, then we can deduce that the term soccer itself carries a positive sentiment.
"""


def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	#lines(tweet_file)

def eng_tweets(tweets_all, key, valuelist):
	return [engtweets for engtweets in tweets_all if engtweets[key] in valuelist]

def cleanup(raw_text):
    cleaned_up = ""
    for char in raw_text:
       if char not in punctuations:
           cleaned_up = cleaned_up + char
    return cleaned_up


def sent_score(w):
	sent_file = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.


  		if w == term:
  			global sum_score
  			sum_score += scores[w]
			#print w, scores[w], 'total:',sum_score

			# if scores[w] > 0:
			# 	global pos_sum
	
			# 	pos_sum += scores[w]
			# 	#print pos_sum

			# elif scores[w] < 0:
			# 	global neg_sum
			# 	neg_sum += scores[w]
			# 	#print neg_sum

			sent.append(w)
  		else:
  			
  			scores[w] =0

  		
  			

	# Print every (term, score) pair in the dictionary
	#print scores.items() 


	
	

if __name__ == '__main__':

	#print "Running sentiment analysis on tweets..."
	main()

	#The set of punctuation in the string module
	punctuations = set(string.punctuation)
	
    #tweets =[rec['text'] for rec in tweets_full if 'text' in rec]
	
  	tweets_full= [json.loads(line) for line in open(sys.argv[2])]
	#print tweets_full[0]
	tweets_all = [rec for rec in tweets_full if 'text' and 'lang' in rec]
	engtweets = eng_tweets(tweets_all, "lang", "en")
	#tweets =[eng['lang'] for eng in tweets if 'lang' in eng] #checking languages of all english tweets.

	#print 'Number of English Tweets: ', len(engtweets)

	tweets = [t['text'] for t in engtweets]

	tweets = tweets [3:5]
	
	# Initialize new dictionary for non_sent terms. key: terms. val: sent_score
	non_sent_dict = {}

	# Initialize new dictionary for non_sent terms. key: terms. val: counter
	non_sent_dub_term = {}


	#For each tweet, print index, content of tweet, parse out content, calculate sent score
	for idx_t, val_t in enumerate(tweets):
		unicode_string = tweets[idx_t]
		#print 'upper:', encoded_string
		encoded_string = unicode_string.encode('utf-8')
		#print 'lower:', encoded_string
		encoded_string = encoded_string.lower()

		
		encoded_string = encoded_string.replace('!', "")
		encoded_string = encoded_string.replace('?', "")
		encoded_string = encoded_string.replace('.', "")
		encoded_string = cleanup(encoded_string)

		d = defaultdict(list)
		splt_tweet = encoded_string.split()

		# Creating new dict to store non-sentiment-carrying terms

		
		non_sent = []
		sent = []
		# Initialize sum to be 0 for every tweet.
		#print idx_t, encoded_string
		pos_sum = 0
		neg_sum = 0
		sum_score = 0
		
		for idx_w, val_w in enumerate(splt_tweet):
			words = splt_tweet[idx_w]

			# Matching words to Sentiment Scores in AFINN-111.txt
			sent_score(words)

		#print 'pos_sum',pos_sum
		#print 'neg_sum', neg_sum


		non_sent_a= [elem for elem in splt_tweet if elem not in (sent)] 

		# Removing Duplicates (Unordered distinct items)
		non_sent_b= list(set(non_sent_a))
		non_sent_score = sum_score


		for val_n in non_sent_b:

			# Add a new term to non_sent_dict if it doesn't exist yet
			if val_n not in non_sent_dict: 
				non_sent_dict[val_n] = non_sent_score
				non_sent_dub_term[val_n] = 1
			
			else:
				non_sent_dub_term[val_n] += 1
				
				non_sent_dict[val_n] = (non_sent_score+ non_sent_dict[val_n])/non_sent_dub_term[val_n]
				#print val_n, non_sent_dub_term

	#print 'non_sent_dict:',non_sent_dict
	for key, val in non_sent_dict.items():
		print key, val

	


		



















