import pandas as pd
import math as m
import numpy as np

# d0 = "preliminary findings in corona research"
# d1 = "novel corona research findings"
# d2 = "new research to corona healing"
# d3 = "regression scikit regression"
# q  = "novel novel preliminary new research"
#
# corpus = [d0, d1, d2, d3, q]
#
# word_bag = sorted(set(d0.split()+d1.split()+d2.split()+d3.split()+q.split()))

d0 = "linear venn venn artificial"
d1 = "linear artificial scikit artificial regression artificial"
d2 = "scikit regression intelligence regression"
d3 = "artificial venn tandem intelligence artificial"
d4 = "regression scikit regression"
q  = "scikit regression artificial"

# d0 = "koblenz university web science data"
# d1 = "koblenz city rheine"
# d2 = "city rheine university"
# d3 = "data science"
# d4 = "university science web"
# d5  = "science computer"

corpus = [d0, d1, d2, d3, d4, q]

word_bag = sorted(set(d0.split()+d1.split()+d2.split()+d3.split()+d4.split()+q.split()))
# calculating tf
def term_frequency(word_bag, corpus):
    data = {}
    for val in word_bag:
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
    df = pd.DataFrame(data, index=corpus)
    return df

tf = term_frequency(word_bag, corpus)
print(tf)

# calculating df

def document_frequency(word_bag, corpus):
    data = {}

    for val in word_bag:
        docCount = 0
        corpusCount = 0

        while corpusCount < (corpus.__len__()-1): # '-1' because we cannot include the terms appearing in q in df; if no q then remove '-1'
            tfd = corpus[corpusCount].split()

            tfdCount = 0

            for word in tfd:
                if val == word:
                     docCount = docCount + 1
                     break

            corpusCount = corpusCount + 1
            data.update({val: docCount})
    return data

df = document_frequency(word_bag, corpus)
print(df)

# calculating tf-idf

def tfidf(tf,df,corpus):
    docCount = corpus.__len__()
    print(docCount - 1)
    count = 0
    finalDf = {}


    while count < docCount:
        tfidfList = []
        for word in word_bag:
            dfVal = df[word]
            # print("document frequency of word %s:%s"%(word,dfVal))
            tfVAl = tf.iloc[count][word]

            print("IDf of %s : %s"%(word, m.log10((docCount-1)/dfVal)))

            tfidfVal = tfVAl * m.log10((docCount-1)/dfVal) #'-1' because total number of document excluding the query, if no query then remove '-1'
            # print(tfidfVal)

            tfidfList.append(tfidfVal)
            # print(tfidfList)
            # print("Term Frequency of %s in d%s:%s"%(word,count, tfVAl))
        finalDf.update({'d'+str(count): tfidfList})
        # print(finalDf)


        count = count + 1
    df = pd.DataFrame(finalDf,index=word_bag)
    return df

weighted = tfidf(tf,df,corpus)
print(weighted)

# Finding Cosine Similarity

def cosineSimilarity(weighted): #manually input the document number
    d = weighted['d0'].array
    q = weighted['d5'].array
    print(q)
    print(d)

    magnitudeD = np.linalg.norm(d)
    print(magnitudeD)

    magnitudeQ = np.linalg.norm(q)
    print(magnitudeQ)

    cosine = np.dot(d,q)/(magnitudeQ * magnitudeD)

    return cosine

cosineValue = cosineSimilarity(weighted)
print('Cosine Similarity: %s'%round(cosineValue,3))


# Rocchio Feedback

def rocchioFeedback(weighted):
    alpha = 1
    beta = 0.8
    gamma = 0.1
    q = weighted['d4'].array #Query
    r = weighted['d1'].array #relevant document
    nr = weighted['d3'].array # non relevant document

    # print(alpha*q)
    # print(beta*r)
    # print(gamma*nr)
    feedback = (alpha * q) + (beta * r) - (gamma * nr) #if more than one relevant and non relevant document then just
                                                # multiply the relevant with relevant and non relevant with non relevant
    print(word_bag)
    return feedback
feedbackValue = rocchioFeedback(weighted)
print(feedbackValue)