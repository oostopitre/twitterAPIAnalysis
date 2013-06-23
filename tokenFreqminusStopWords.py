""" Calculates token frequency in all tweets, minus stop words """

TWEET_FILE = open(r'D:\Dropbox\twitter\usTweets.json','r')

def get_english_stops():
    """ Get English stop words from NLTK and return as a set """
    from nltk.corpus import stopwords
    english_stops = set(stopwords.words('english'))
    return english_stops
    
def token_freq(tokens):
    """ Frequency distribution of tokens """
    from collections import defaultdict
    freq = defaultdict(int)
    for token in tokens:
        freq[token] += 1
    return freq
    
def print_dashed_line(line_length):
    """ Prints dashed line of passed length """
    print '\n', '-' *line_length
    
def main():
    """ Core module """    
    
    import ast
    from nltk.tokenize import RegexpTokenizer
    from collections import Counter
    
    tokenizer = RegexpTokenizer(r'\s+', gaps=True)
    
    english_stops = get_english_stops()
    
    total_tokens = []
    sleep_tokens = []
    total_tweets = 0
    sleep_tweets = 0
    
    for line in TWEET_FILE.readlines(): 
        tweet = ast.literal_eval(line)
        tweet = tweet['text'].encode('utf-8')
        new_tokens = [t.lower() for t in tokenizer.tokenize(tweet)
                        if t.lower() not in english_stops and len(t)>3]
        total_tokens += new_tokens
        total_tweets += 1
        print total_tweets
        if 'sleep' in new_tokens:
            #print newTokens
            sleep_tokens += new_tokens
            sleep_tweets += 1
#            if sleep_tweets % 10 == 0:
#                break

    print_dashed_line(50)
    print "Total Tweets: ", total_tweets
    print "Sleep Tweets: ", sleep_tweets
    print "Total Tokens: ", len(total_tokens)
    print "Sleep Tokens: ", len(sleep_tokens)
    print_dashed_line(50)
    
    print_dashed_line(50)
    print 'Most Common Total:'
    print_dashed_line(50)
    for token, count in  Counter(token_freq(total_tokens)).most_common(100):
        print '%s \t %7d' % (token, count)

    print_dashed_line(50)
    print 'Most Common Sleep:'
    print_dashed_line(50)
    for token, count in  Counter(token_freq(sleep_tokens)).most_common(100):
        print '%s \t %7d' % (token, count)    
    
 
if __name__ == '__main__':
    main()



0
