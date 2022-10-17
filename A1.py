#f = open('json_sample.txt','r')

import json
import string

#####

# import these modules
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

from nltk.tokenize import sent_tokenize, word_tokenize #pip install nltk or python -m pip install nltk
   
ps = PorterStemmer()
ls=LancasterStemmer()

  
# choose some words to be stemmed
#words = ["program", "programs", "programmer", "programming", "programmers"]
  
'''for w in words:
    print(w, " : ", ps.stem(w))'''

#######

with open('json_sample.txt') as f:
    contents = f.readline() #readline for one docu dict, read for all of them
    dictContents = json.loads(contents)
    print(contents)   
#    for key in dictContents:
#        print(key)
    #print(dictContents["id"])
#    print(dictContents["plain"])

    plainWords = dictContents["plain"].split()
    #print(plainWords)
    
    tf = {}
    counter = 1
    
    for word in plainWords:
        word = word.upper().translate(str.maketrans('', '', string.punctuation))
        if word not in tf:
            counter=1
            tf[word]=counter
        else:
            tf[word]+=1

    sortedWords=sorted(tf.keys(), key=lambda x:x.lower())

    #print(tf)
    print(sortedWords, "\n", len(tf)) # 97 terms combined caps, 

    ##
    for w in sortedWords:
        print(w, " -ps- ", ps.stem(w), " -ls- ", ls.stem(w))
        