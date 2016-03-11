import oauth2 as oauth
import time
import random
import json
import math
import sys
import pprint

def grab_tweet():
  query = '%20'.join(sys.argv[1:])
  # Set the API endpoint
  url = "https://api.twitter.com/1.1/search/tweets.json?q=" + query
  token = oauth.Token("1035256117-JEcbtW3741GwyB820PmCHLCvq0Us18FhNSZdDBH", "8kpKfpzwVDGEKZFswcLHFVWylCripMILo3SxKLfIenX8Q")
  consumer_key = '2VpE9wyPHAnfvz5aBF44G59Z4'
  consumer_secret = 'C35EaRzDgk0Kf6vfxiLHXrFNlK5RnjqSBLCDoxnhG4DqksnqVY'
  request_token_url = 'https://api.twitter.com/oauth/request_token'
  access_token_url = 'https://api.twitter.com/oauth/access_token'
  authorize_url = 'https://api.twitter.com/oauth/authorize'
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  client = oauth.Client(consumer)
  # Request token URL for Twitter.
  request_token_url = "https://api.twitter.com/1.1/search/tweets.json?q=" + query
  # Create our client.
  client = oauth.Client(consumer, token)
  # The OAuth Client request works just like httplib2 for the most part.
  resp, content = client.request(request_token_url, "GET")
  #pretty print the JSON string
  parsed = json.loads(content)
  #print json.dumps(parsed, indent=4, sort_keys=True)

  #convert response stringified JSON to python dict
  j = '{"action": "print", "method": "onData", "data": '+ content +'}'
  class Payload(object):
       def __init__(self, j):
           self.__dict__ = json.loads(j)
  p = Payload(j)

  #get psuedorandom tweet from selected
  data_count = p.data['search_metadata']['count']
  random_id = int(math.floor(data_count*random.random()))
  tweet_url = p.data['statuses'][random_id]

  print "Your search for '%s' returned %d tweets. This is the data for random tweet number %s:" % (query, data_count, random_id)
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(tweet_url)

grab_tweet()