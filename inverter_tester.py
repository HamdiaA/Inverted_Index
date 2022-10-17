import json, string, time

loop = True
totalTime = 0
numOfRuns = 0
avgTime = 0

while loop:
    startTime = time.time()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    word = input("Enter searchword: ").upper()
    if word == "ZZEND":
        avgTime = totalTime / numOfRuns
        print("\nAverage time taken to generate results " + str(avgTime) + " seconds")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        loop = False
    else:
        with open('document_frequency.txt', 'r+b') as f1:
            Lines = f1.readlines()
            for line in Lines:
                fixedLine = line.decode(errors='ignore').replace("\r\n","")
                colon = fixedLine.index(":")
                term = fixedLine[:colon]
                df = fixedLine[colon+2:]
                if word == term:
                    print("Document Frequency: " + df)
        with open('invertedIndex.txt', 'r+b') as f2:
            Lines = f2.readlines()
            for line in Lines:
                fixedLine = line.decode(errors='ignore').replace("\r\n","")
                colon = fixedLine.index(":")
                term = fixedLine[:colon]
                termOccurance = fixedLine[colon+2:]
                if word == term:
                    print("Documents the term occurs in with the document title: " + termOccurance)
                    endTime = time.time()
                    timeTaken = endTime - startTime
                    print("\nResults generated in " + str(timeTaken) + " seconds")
                    totalTime += timeTaken
                    numOfRuns += 1

                    # hey mahdi