
from nltk.corpus import stopwords
from stemming.porter2 import stem
import string
import re

def process(text):
    print("IN PREPROCESS", text)
    # lower case all words
    text = text.lower()
 
    # remove all punctuation
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text = regex.sub('', text)
    
    # remove all digits
    regex = re.compile('[%s]' % re.escape(string.digits))
    text = regex.sub('', text)
    
    
    # only retain words >= 4 characters long
    text = ' '.join([word for word in text.split() if (len(word)>=4)])
  
    # remove stop words
    #sw = stopwords.words("english")
    #text = ' '.join([word for word in text.split() if word not in sw])
    
    # convert to stem words
    #text = ' '.join([stem(word) for word in text.split()])
   
    
    # only retain unique words
   # text = ' '.join(set(text.split()))
    
    return text