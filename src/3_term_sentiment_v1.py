# $ python term_sentiment.py <sentiment_file> <tweet_file>
import sys
import json


def createSentiDict(sf):
    with open(sf) as inputFile:
        scores = {} # initialize an empty dictionary
        for line in inputFile:
            term, score  = line.split("\t")  # The file is tab-delimited.
            scores[term] = int(score)  # Convert the score to an integer.
        return scores

def allocateSenti(tf,scores):
    with open(tf) as inputFile:
        datalist=[]
        for line in inputFile:
            datalist.append(json.loads(line))
        scoresExt = {} # initialize a dict for new words
        for item in datalist:
            senti=0
            if 'text' in item.keys():
                tweet=item['text'].encode('utf-8')
                words = tweet.split()
                for word in words:
                    if word in scores.keys():
                        senti+=float(scores[word])
                # Creating scores for missing words in AFINN.txt
                # Could use a better code than cumulating sentiments
                # cleanup for Cases, periods, ... other random letters
                for word in words:
                    if word not in scores.keys():
                        if word not in scoresExt.keys():
                            scoresExt[word]=senti
                        else:
                            scoresExt[word]+=senti
            #print senti
        #printing the newly created dict with missing scores in scores Dict
        for key in scoresExt:
            print key, scoresExt[key]


def lines(fp):
    fpObj = open(fp)
    print str(len(fpObj.readlines()))

def main():
    senti_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = createSentiDict(senti_file)
    allocateSenti(tweet_file, scores)


if __name__ == '__main__':
    main()
