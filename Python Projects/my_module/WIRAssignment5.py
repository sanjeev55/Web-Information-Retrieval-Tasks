import pandas as pd

d1 = "vaccine research corona virus research"
d2 = "research research cancer vaccine vaccine"
d3 = "virus virus corona vaccine lab"
d4 = "cancer lab research lab"

q1 = "vaccine vaccine research cancer"
q2 = "vaccine research"

corpus = [d1, d2, d3, d4]
# print(corpus.__len__())

corpusSize = corpus[0].split().__len__()+corpus[1].split().__len__()+corpus[2].split().__len__()+corpus[3].split().__len__()
# print(corpusSize)

word_bag = set(d1.split()+d2.split()+d3.split()+d4.split())
sortedWordBag = sorted(word_bag)
# print(sortedWordBag)

def term_frequency(sortedWordBag, corpus):
    data = {}
    for val in sortedWordBag:
        corpusCount = 0
        list = []
        while corpusCount < corpus.__len__():
            tfd = corpus[corpusCount].split()
            tfdCount = 0

            for word in tfd:
                if val == word:
                    tfdCount = tfdCount + 1

            corpusCount = corpusCount + 1
            list.append(tfdCount)
            data.update({val: list})
    df = pd.DataFrame(data, index=['d1','d2','d3','d4'])
    return df
tfDf = term_frequency(sortedWordBag, corpus)
print("Term Frequency dataframe")
print(tfDf)
# print(tfDf["research"].sum())


def probCorpus():
    listPMC = {}
    for val in sortedWordBag:
        termCount = tfDf[val].sum()
        # print(termCount)
        pMc = termCount / corpusSize
        # print("The value of P_Mc(%s) is %s"%(val,pMc))
        listPMC.update({val:pMc})
    # print(listPMC)
    return listPMC
eachTermProbCorpus = probCorpus()
print("\nList of Probability of each term given the whole corpus: P(t|Mc)")
print(eachTermProbCorpus)

# print(tfDf['research'].values[0])

def probTermDoc():
    pMdData = {}
    for val in sortedWordBag:
        count = 0
        listofVal =[]
        while count < corpus.__len__():
            termCount = tfDf[val].values[count]
            # print(termCount)
            docTerm = tfDf.values[count].sum()
            # print(docTerm)

            pMd = termCount/docTerm
            listofVal.append(pMd)
            pMdData.update({val: listofVal})
            count = count+1

            # print("the PMd(t) value for the term %s for document d%s is: %s "%(val,count,pMd))
        # print(listofVal)
    newdf = pd.DataFrame(pMdData, index=['d1','d2','d3','d4'])
    return newdf


probEachTerm = probTermDoc()
print("\nDataframe of probability of each term given a document model: P(t|Md)")
print(probEachTerm)

# Ranking Document
queryList1 = q1.split()
queryList2 = q2.split()
# print(queryList1)

def rankedDocument(query):
    count = 0

    rankedList = {}
    while count < corpus.__len__():
        pqd = 1
        for val in query:
            # print("Value:%s"%val)
            pMd = probEachTerm[val].values[count] #This finds the pMd fo a term from the data frame i created
            # print("PMD:%s"%pMd)
            pqd = pqd * pMd
            # print("PQD:%s"%pqd)

            rankedList.update({count+1: pqd})
        count = count + 1
    return rankedList

wholeRankedDocumentForQuery1 = rankedDocument(queryList1)
wholeRankedDocumentForQuery2 = rankedDocument(queryList2)
print("\n List of Ranked documents based on Query 1")
print(wholeRankedDocumentForQuery1)
print("\n List of Ranked documents based on Query 2")
print(wholeRankedDocumentForQuery2)

# Smoothing

def smoothing(lamda):

    newKeyValue = {}
    for val in sortedWordBag:
        count = 0
        listOfData = []
        while count < corpus.__len__():
            ptmd = probEachTerm[val].values[count]
            ptmc = eachTermProbCorpus.get(val)
            ptd = lamda * ptmd + (1 - lamda )* ptmc
            listOfData.append(ptd)
            count = count + 1
            newKeyValue.update({val: listOfData})
    newdf = pd.DataFrame(newKeyValue, index=['d1','d2','d3','d4'])
    return newdf

smoothdf = smoothing(0.5)
print("\n Dataframe after applying Smoothing")
print(smoothdf)

def rankedSmooth(query):
    count = 0

    rankedList = {}
    while count < corpus.__len__():
        pqd = 1
        for val in query:
            # print("Value:%s"%val)
            pMd = smoothdf[val].values[count]
            # print("PMD:%s"%pMd)
            pqd = pqd * pMd
            # print("PQD:%s"%pqd)

            rankedList.update({count+1: pqd})
        count = count + 1
    return rankedList

smoothRankedDocumentForQuery1 = rankedSmooth(queryList1)
smoothRankedDocumentForQuery2 = rankedSmooth(queryList2)
print("\nList of document's rank (descending) after smoothing based on Query 1")
print({k: v for k, v in sorted(smoothRankedDocumentForQuery1.items(), key=lambda item: item[1], reverse=True)}) #normally sorted() sorts list in ascending order 'reverse = True' sorts list in descending order
# [0.0007, 0.0047, 0.0003, 0.0005]
print("\nList of document's rank (ascending) after smoothing based on Query 2")
print({k: v for k, v in sorted(smoothRankedDocumentForQuery2.items(), key=lambda item: item[1])})
# [0.0681, 0.1012, 0.0270, 0.0270]

# Top most ranked:
print("\nCalculating average value to find top most ranked model")
def mostRanked():
    count = 1
    while count <= corpus.__len__():
        average = (wholeRankedDocumentForQuery1.get(count)+wholeRankedDocumentForQuery2.get(count)+smoothRankedDocumentForQuery1.get(count)+smoothRankedDocumentForQuery2.get(count))/4

        print("average for d%s is : %s"%(count,average))
        count = count + 1
finalResult = mostRanked()
