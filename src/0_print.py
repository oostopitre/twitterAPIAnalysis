import urllib
import json
import sys

def fetchTweets(keywordSearch,nPages):
    response = urllib.urlopen("http://search.twitter.com/search.json?q="+ \
    keywordSearch+"&page="+nPages)
    #print type(response)
    data = json.load(response)
    tweets = data["results"]


    for i in tweets:
        print i["text"]

##    Debugging
##    # prints the type of the data object
##    print type(data)
##    # prints the keys available in the 'data' dict
##    print data.keys()
##    print
##
##    #prints the type of the data in the 'results' key
##    print type(data["results"])
##    #print tweets
##
##    #prints the first object of the list
##    print data["results"][0]
##    print
##    print data["results"][0].keys()
##    print

def main():
    keywordSearch = sys.argv[1]
    nPages = sys.argv[2]
    fetchTweets(keywordSearch,nPages)

if __name__ == '__main__':
    main()