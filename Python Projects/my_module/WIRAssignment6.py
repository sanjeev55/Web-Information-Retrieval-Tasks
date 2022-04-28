import pandas as pd
from bs4 import BeautifulSoup

d1 = BeautifulSoup(open("Document1.html"),features="lxml")
d2 = BeautifulSoup(open("Document2.html"),features="lxml")
d3 = BeautifulSoup(open("Document3.html"),features="lxml")
d4 = BeautifulSoup(open("Document4.html"),features="lxml")
d5 = BeautifulSoup(open("Document5.html"),features="lxml")

corpus = [d1, d2, d3, d4, d5]
print(corpus.__len__())


def zoneParser(document):
    count = 1
    parsedDocuments = {}
    introList = []
    abstractList = []
    titleList = []
    for d in document:
        title  = d.find('title')

        title = title.find(text=True)

        print("Tile of document:::::::::: "+title)

        abstract = d.find('b')

        abstractContent = abstract.find_next_sibling(text=True)
        # print("Abstract of document:::::::::: "+abstractContent)

        introduction = d.find('h2')

        introductionContent = introduction.find_next('p').find(text=True)
        # print(introductionContent)

        introList.append(str(introductionContent))
        titleList.append(str(title))
        abstractList.append(str(abstractContent))

    parsedDocuments.update({"Title":titleList})
    parsedDocuments.update({"Intro":introList})
    parsedDocuments.update({"Abstract":abstractList})

    df = pd.DataFrame(parsedDocuments,index=['d1','d2','d3','d4','d5'])

    return df


newdf = zoneParser(corpus)

print(zoneParser(corpus))

bow = ['auditory','and','visual','eye','performance','method']

def zoneIndex(bow):


    for w in bow:
        count = 0
        print(w)

        title = newdf['Title'].values[count]
        abstract = newdf['Abstract'].values[count]
        intro = newdf['Intro'].values[count]
        title = title.replace('\n','').lower().split()
        print(title)
        intro = intro.replace('\n','').lower().split()
        print(intro)
        abstract = abstract.replace('\n','').lower().split()
        print(abstract)
        wordCountIntro = 0
        wordCountTitle = 0
        wordCountAbstract = 0
        for t in title:
            if w == t:
                 wordCountTitle = wordCountTitle+1
        for i in intro:
            if w == i:
                 wordCountIntro = wordCountIntro + 1
        for a in abstract:
            if w == a:
                wordCountAbstract = wordCountAbstract + 1
        print(wordCountTitle)
        print(wordCountIntro)
        print(wordCountAbstract)


print(zoneIndex(bow))



