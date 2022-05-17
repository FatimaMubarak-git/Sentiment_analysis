
import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords

import numpy as np

# download the twitter samples and stopwords(and, has, have, about, the…) 
nltk.download('twitter_samples')
nltk.download('stopwords')


# save the positive tweets in all_positive_tweets strings and negative tweets in all_negative_tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


 # print some tweet samples to check how they are gonna be shown. 
 # The positive tweets will be shown in green color, and the negative ones are in red :


np.random.seed(2)
rand = np.random.randint(0,5000,2)

print("Positive tweets:")
print('\033[92m')
for i in rand:
  print(all_positive_tweets[i])
BEIRUT AI (AMBASSODER, MEMBERSHIP)
  print("Negative tweets:")
print('\033[91m')
for i in rand:
  print(all_negative_tweets[i])

  