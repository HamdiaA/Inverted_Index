import json, string
#from collections import Counter

f2 = open('document_frequency.txt','w')
f3 = open('occFreq.txt','w')
f4 = open('invertedIndex.txt','w')
f5 = open('term_frequency.txt','w')


with open('json_small_sample.txt', 'r+b') as f:
    Lines = f.readlines()
    df = {}
    docTermOccurence = {}
    termPosition = {}
    allPositions = {}
    tempArray = []
    postingsList = {}


    for line in Lines:
        dictContents = json.loads(line)
        docIDNum = dictContents["id"]
        docTitleName = dictContents["title"]
        plainWords = dictContents["plain"].split()
        tf = {}
        counter = 0
        positionsInCurrentDoc = {}

        for word in plainWords:
            word = word.upper().translate(str.maketrans('', '', string.punctuation))
            counter += 1

            if word not in df:
                df[word] = 1 
                docTermOccurence[word] = [str(docIDNum) + ": " + docTitleName]
            elif word not in tf and word in df:
                df[word] += 1
                docTermOccurence[word] += [str(docIDNum) + ": " + docTitleName]

            if word not in tf:
                tf[word] = 1
                positionsInCurrentDoc[word] = [counter]
            else:
                tf[word] += 1
                positionsInCurrentDoc[word] += [counter]


            if allPositions.get(word) is None:# or (str([docIDNum, positionsInCurrentDoc.get(word)]) not in str(allPositions[word])):
                allPositions[word] = [docIDNum, positionsInCurrentDoc.get(word)]
            else:
                allPositions[word] += [docIDNum, positionsInCurrentDoc.get(word)] #tf[word]]

        '''for word in plainWords:
            if postingsList[word] == None:
                postingsList[word] = []'''

    #f.close()

    #f2.write(allPositions)

    #with open("myfile.txt", 'w') as f:
    #sortedtf=dict(sorted(tf.items(), key=lambda x:x[0]))
    #print(sortedtf)
    sorteddf=dict(sorted(df.items(), key=lambda x:x[0]))
    print(sorteddf)
    sorteddocTermOccurence= dict(sorted(docTermOccurence.items(), key=lambda x:x[0]))
    #print(sorteddocTermOccurence)
    #print(allPositions)

    for key, value in sorteddf.items():
        f2.write('%s: %s\n' % (key, value))

    for key, value in allPositions.items():
        f3.write('%s: %s\n' % (key, value))

    for key, value in sorteddocTermOccurence.items():
        f4.write('%s: %s\n' % (key, value))


 
    # word : [[[123, [1,8,9]], [456, [11, 35]]]


    # word : [123,[1], [123,[2]]]
    # word : [123,[1, 2]]



    # The brown dog jumped over the lazy brown fox.  
    # The brown man is dumb.


    # 


    
    #[word: (docIDNum = 1, positions)] --> positions.append(counter)

    #[1, 2]


    # Belgium : [[1 , [4,5]], [2, [20, 22]]]