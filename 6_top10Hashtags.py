"""
Program to compute the top 10 hash tags from
a twitter livestream
"""
# $ python 6_top10Hashtags.py <tweet_file>
import sys
import json

# Creates a dictionary of sentiment words: score from the text file
def computeHashtags(tf):
     with open(tf) as inputFile:
        datalist=[]
        # reading the twitter streaming data record by record
        for line in inputFile:
            datalist.append(json.loads(line))
            freqHashtags = {} # initialize a dict for holding hashtags
        #Hashtag is embedded in item-->dict.entities-->listofdicts.hashtags-->
        #-->key='text'
        for item in datalist:
            if 'entities' in item.keys():
                entities = item['entities'] #entities object is a dict
                hashtags = entities['hashtags'] # hashtags is a list of dicts.
                #Each dict is a hashtag
                for each in hashtags:
                    if len(each)>0:
                        hashtext = each['text']
                        if hashtext not in freqHashtags.keys():
                            freqHashtags[hashtext]=1
                        else:
                            freqHashtags[hashtext]+=1
        #Sorting the final dict on 'value' in descending order and printing \
        #the hashtag, frequency for the top 10 elements
        for item in sorted(freqHashtags, key = freqHashtags.get , reverse=True)[:10]:
            print '%s' '%8.4f' \
            % (item, freqHashtags[item])

def main():
    tweet_file = sys.argv[1]
    computeHashtags(tweet_file)

if __name__ == '__main__':
    main()