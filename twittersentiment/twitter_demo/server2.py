import json
import sys
from collections import defaultdict


from TwitterSearch import TwitterSearchOrder
import indicoio
from pprint import pprint

from twitter_demo.twitter import TwitterClient
import twitter_demo.settings as settings

    
indicoio.config.api_key = "2e559e40a6ebea9dddb39e753363f6e1"
query_string = sys.argv[1:]
query = TwitterSearchOrder()
query.set_keywords(query_string)
query.set_language('en')
query.set_include_entities(False)
results = TwitterClient.search_tweets(query)

#print results['content']['statuses'][0].keys()

#tweets = [tweet['text'] for tweet in results['content']['statuses']]
tweets = []

for tweet in results['content']['statuses']:
	data = {
		'tweet_id': tweet['id_str'],
		'tweet_text': tweet['text']
	}
	req = urllib2.Request('http://45.33.90.42:3000/insert_data')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	tweets.append(data) 

	
sentiment = indicoio.batch_sentiment(tweets)
pairs = sorted(zip(sentiment, tweets))
n_tweets = float(len(pairs))

top_n = 5
most_negative = pairs[:top_n]
#most_positive = list(reversed(pairs[-top_n:]))

data = {
    #'most_positive': most_positive,
    'most_negative': most_negative,
    #'average': sum(sentiment)/n_tweets
}

pprint(zip(tweets))
