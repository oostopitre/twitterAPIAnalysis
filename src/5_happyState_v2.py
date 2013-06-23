"""
So there are several enhancements that can be done to thsi assignment
1. From the live-stream extract only tweets from a bounding box: Just USA with:
    url = "https://stream.twitter.com/1/statuses/filter.json?locations=-170.0,18.0,-60.0,72.0"
2. Search for the tweet location from either of the three location in the twitter object
    coordinates object or
    place field of the user object or
    location field of the tweet object
3. Also enhance by not just searching for two letter state but city names as well
3. Normalize the score to adjust for number of tweets. Some Average metric?
4. Average sentiment only over non-zero sentiments?
5. Removing stop words from the tweets

"""
# $ python tweet_sentiment.py <sentiment_file> <tweet_file>
import sys
import json

def main():
    senti_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = createSentiDict(senti_file)
    analyzeTweet(tweet_file, scores)

if __name__ == '__main__':
    main()

# Creates a dictionary of sentiment words: score from the text file
def createSentiDict(sf):
    with open(sf) as inputFile:
        scores = {} # initialize an empty dictionary
        for line in inputFile:
            term, score  = line.split("\t")  # The file is tab-delimited.
            scores[term] = int(score)  # Convert the score to an integer.
        return scores

#Allocates sentiment score for each tweet message
def allocateSenti(tweet,scores):
    senti=0
    words = tweet.split()
    for word in words:
        if word in scores.keys():
            senti+=float(scores[word])
    return senti

def analyzeTweet(tf, scores):
    with open(tf) as inputFile:

        states = { 'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas',\
        'AS': 'American Samoa','AZ': 'Arizona','CA': 'California',\
        'CO': 'Colorado','CT': 'Connecticut','DC': 'District of Columbia',\
        'DE': 'Delaware','FL': 'Florida','GA': 'Georgia','GU': 'Guam',\
        'HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana',\
        'KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts',\
        'MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota',\
        'MO': 'Missouri','MP': 'Northern Mariana Islands','MS': 'Mississippi',\
        'MT': 'Montana','NA': 'National','NC': 'North Carolina',\
        'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire',\
        'NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada',\
        'NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon',\
        'PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island',\
        'SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee',\
        'TX': 'Texas','UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands',\
        'VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin',\
        'WV': 'West Virginia','WY': 'Wyoming'}

        #load the full twitter data from the live stream
        datalist=[]
        for line in inputFile:
            datalist.append(json.loads(line))

        result = {} #dictionary to hold state:aggregate sentiment score
        for itemtweet in datalist:
            if 'user' in itemtweet.keys():
                #extraction location field from user object
                loc = itemtweet['user']['location'].split()
                for itemloc in loc:
                    #check if the location field is in states dict
                    if itemloc in states.keys():
                        #print itemloc, itemtweet['text'], \
                        #allocateSenti(itemtweet['text'], scores)

                        #allocate sentiment for that tweet
                        senti=allocateSenti(itemtweet['text'], scores)
                        result[itemloc]=result.get(itemloc,0)+senti
        #print result

        # find the maximum score hence happiest state
        for key in result.keys():
            cur=result[key]
            max=0
            if(cur>max):
                max=cur
                state = key
        print state




