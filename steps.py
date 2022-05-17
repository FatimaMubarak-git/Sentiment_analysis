
import re
import string

from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


# Our next objective is to perform Data preprocessing which a series of steps that attempt to remove words that are mean nothing and unnecessary :

# -Lowercasing every sample

# -Removing every stopword and punctuation

# -Stemming

# -Splitting the words in a sample into an array of strings

def process_tweet(tweet):
  stemmer = PorterStemmer() 
  stopwords_english = stopwords.words('english')

  # remove the stock market tickers
  tweet = re.sub(r'\$\w*', '', tweet)

  # remove the old styles retweet text 'RT'
  tweet = re.sub(r'^RT[\s]+', '', tweet)

  # remove the hyperlinks
  tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

  # remove the # symbol
  tweet = re.sub(r'#', '', tweet)

  # Tokenize the tweet
  tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
  tweet_tokens = tokenizer.tokenize(tweet)

  tweet_clean = []

  # removing stopwords and punctuation
  for word in tweet_tokens:
    if (word not in stopwords_english and
        word not in string.punctuation):
      stem_word = stemmer.stem(word)  
      tweet_clean.append(stem_word)

  return tweet_clean


# apply Data Preprocessing on random sample from the training set :
  tweet = all_positive_tweets[np.random.randint(0,5000)]
print('Raw tweet :\n', tweet)
tweet =process_tweet(tweet)
print('After processing the tweet : \n',tweet)




# Now we want to make a word dictionary counter. This counter counts how many times every word was present either in 
# the positive or in the negative data sets. The set of words are already labled with 1 for postive and 0 for negative, 
# whenever a word is present its positive or negative counter is incremented
def count_tweets(tweets, ys):
  ys_list = np.squeeze(ys).tolist()
  freqs ={}

  for y, tweet in zip(ys_list, tweets):
    for word in process_tweet(tweet):
      pair = (word, y)
      if pair in freqs:
        freqs[pair] +=1
      else:
        freqs[pair] = 1
  
  return freqs


# This function shows the negative and positive counter of a specific word if needed :
def lookup(freqs, word, label):
  n = 0
  pair = (word, label)
  if pair in freqs:
    n = freqs[pair]
  return n 

