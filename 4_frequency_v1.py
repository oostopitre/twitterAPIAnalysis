# $ python frequncy.py <tweet_file>
import sys
import json


def freqHistogram(tf):
    with open(tf) as inputFile:
        datalist=[]
        for line in inputFile:
            datalist.append(json.loads(line))
        freq = {} # initialize a dict for new words
        for item in datalist:
            if 'text' in item.keys():
                tweet=item['text'].encode('utf-8').replace('\n','')
                words = tweet.split()
                #creating a frequency dict for unique words
                for word in words:
                    cleanword=word.strip()
                    if word not in freq.keys():
                        freq[cleanword]=1
                    else:
                        freq[cleanword]+=1
        #Computing the total
        total=0
        for key in freq:
            total = float(total) + freq[key] #Calculate total word occurences
        #normalizing the Histogram
        for key in freq:
            #print '%s' '%10.0f' % (key, freq[key])
            print '%s' '%8.4f' \
            % (key, freq[key]/total)

def main():
    tweet_file = sys.argv[1]
    freqHistogram(tweet_file)


if __name__ == '__main__':
    main()
