import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')

retrieved = df["retrieved"]

# -----------Gold Standard-------------
GSetosa = df[df["gold_standard"] == "setosa"]
# print(GSetosa["gold_standard"].count())
GVersicolor = df[df["gold_standard"] == "versicolor"]
# print(GVersicolor["gold_standard"].count())
GVirginica = df[df["gold_standard"] == "virginica"]
# print(GVirginica["gold_standard"].count())

# ------------Retrieved-------------------
ASetosa = df[df["retrieved"] == "setosa"]
# print(ASetosa["retrieved"].count())
AVersicolor = df[df["retrieved"] == "versicolor"]
# print(AVersicolor["retrieved"].count())
AVirginica = df[df["retrieved"] == "virginica"]
# print(AVirginica["retrieved"].count())

# ------------Intersection Between Gold Standard and Retrieved------------------
ISetosa = df[(df["retrieved"] == "setosa") & (df["gold_standard"] == "setosa")]
# print(ISetosa.count())
IVersicolor = df[(df["retrieved"] == "versicolor") & (df["gold_standard"] == "versicolor")]
# print(IVersicolor.count())
IVirginica = df[(df["retrieved"] == "virginica") & (df["gold_standard"] == "virginica")]
# print(IVirginica.count())

# Precision-------------
def precision(Intersection, Retrieved):
    precisionVal = Intersection/Retrieved
    return precisionVal

pSetosa = precision(ISetosa.count(),ASetosa.count())
pVersicolor = precision(IVersicolor.count(),AVersicolor.count())
pVirginica = precision(IVirginica.count(),AVirginica.count())
print("Setosa Precision: %s"%pSetosa)
print("Versicolor Precision: %s"%pVersicolor)
print("Viriginca Precision: %s"%pVirginica)


# Recall-------------------
def recall(Intersection, GoldStandard):
    recallVal = Intersection/GoldStandard
    return recallVal


rSetosa = recall(ISetosa.count(),GSetosa.count())
print("Setosa Recall: %s"%rSetosa)
rVersicolor =recall(IVersicolor.count(),GVersicolor.count())
print("Versicolor Recall:%s"%rVersicolor)
rVirginica = recall(IVirginica.count(),GVirginica.count())
print("Verginica Recall:%s"%rVirginica)

# F1-Score------------------

def f1Score(precision,recall):
    f1Val = (2*precision*recall)/(recall+precision)
    return f1Val

fSetosa = f1Score(pSetosa,rSetosa)
print("Setosa F1 Score: %s"%fSetosa)
fVersicolor = f1Score(pVersicolor,rVersicolor)
print("Versicolor F1 ScoreL %s"%fVersicolor)
fViriginca = f1Score(pVirginica,rVirginica)
print("Virginica F1 Score: %s"%fViriginca)

# Accuracy--------------------
def accuracyCal(name,intersection):
    uSetosa = df[(df["retrieved"] == name) | (df["gold_standard"] == name)]
    print(uSetosa)#Finding Union of gold standard and retrieved.

    tnSetosa = retrieved.count() - uSetosa.count()
    print(tnSetosa)#Finding true negative

    aSetosa =(intersection["retrieved"].count() + tnSetosa) / retrieved.count() #calculating accuracy
    print("Accuracy %s: %s"%(name,aSetosa))

    return aSetosa['retrieved']

accuracySetosa = accuracyCal('setosa',ISetosa)
print(accuracySetosa)
accuracyvirginica = accuracyCal('virginica',IVirginica)
print(accuracyvirginica)
accuracyVersicolor = accuracyCal('versicolor',IVersicolor)
print(accuracyVersicolor)

print((accuracySetosa+accuracyvirginica+accuracyVersicolor)/3)


# def getConfusionMatrix(retreieved, goldStandard):
#     confusionMatrix = np.zeros((3,3))
#
#     for predicted, real in zip(retrieved, goldStandard):
#         if predicted == 'setosa':
#             if predicted == real:
#                 confusionMatrix[0,0] += 1
#             elif real == 'virginica':
#                 confusionMatrix[0,1] += 1
#             else:
#                 confusionMatrix[0,2] += 1
#         elif predicted == 'virginica':
#             if predicted == real:
#                 confusionMatrix[1,1] += 1
#             elif real == 'setosa':
#                 confusionMatrix[1,0] += 1
#             else:
#                 confusionMatrix[1,2] += 1
#         else:
#             if predicted == real:
#                 confusionMatrix[2,2] += 1
#             elif real == 'setosa':
#                 confusionMatrix[2,0] += 1
#             else:
#                 confusionMatrix[2,1] += 1
#     return confusionMatrix
#
# def accuracy(retrieved, goldStandard):
#     confMat = getConfusionMatrix(retrieved, goldStandard)
#     acc = np.sum(np.diag(confMat)/np.sum(confMat))
#     return acc
#
# print(accuracy(retrieved, goldStandard))

# Precision @ 10----------------

newDf = df.head(10) #getting the first 10 rows of the dataframe
# print(newDf)
newGSetosa = newDf[newDf["gold_standard"] == "setosa"]
# print(newGSetosa["gold_standard"].count())
newGVersicolor = newDf[newDf["gold_standard"] == "versicolor"]
# print(newGVersicolor["gold_standard"].count())
newGVirginica = newDf[newDf["gold_standard"] == "virginica"]
# print(newGVirginica["gold_standard"].count())

newASetosa = newDf[newDf["retrieved"] == "setosa"]
# print(newASetosa["retrieved"].count())
newAVersicolor = newDf[newDf["retrieved"] == "versicolor"]
# print(newAVersicolor["retrieved"].count())
newAVirginica = newDf[newDf["retrieved"] == "virginica"]
# print(newAVirginica["retrieved"].count())


newISetosa = newDf[(newDf["retrieved"] == "setosa") & (newDf["gold_standard"] == "setosa")]
# print(newISetosa.count())
newIVersicolor = newDf[(newDf["retrieved"] == "versicolor") & (newDf["gold_standard"] == "versicolor")]
# print(newIVersicolor.count())
newIVirginica = newDf[(newDf["retrieved"] == "virginica") & (newDf["gold_standard"] == "virginica")]
# print(newIVirginica.count())

newPSetosa = precision(newISetosa.count(),newASetosa.count())
print("Setosa precision @10: %s"%newPSetosa)
newPVersicolor = precision(newIVersicolor.count(),newAVersicolor.count())
print("Versicolor precision @ 10: %s"%newPVersicolor)
newPVirginica = precision(newIVirginica.count(),newAVirginica.count())
print("Virginica precision @ 10: %s"%newPVirginica)




# MAP---------------------------

# -------Function to find the average precision of each data--------------------
def avgPrecision(name):
    count = 0
    cutoffValue = 0
    precisionValue = 0

    while count < retrieved.count():
        # print("inside while loop")
        currentdf = df.iloc[count]
        # print(currentdf)
        if (currentdf["retrieved"] == name) & (currentdf["gold_standard"] == name):
            # print("inside if==================---------")
            # print("countVALUE:::::: %s"%count)
            totaldf = df.head(count+1)
            # print(totaldf)
            retrievedVal = totaldf["retrieved"]
            # print(retrievedVal["gold_standard"].count())
            intersection = totaldf[(totaldf["retrieved"] == name) & (totaldf["gold_standard"] == name)]
            # print(intersection["gold_standard"].count())

            newPrecisionValue = precision(intersection.count(),retrievedVal.count())
            # print(" newPrecisionValue%s"%newPrecisionValue)
            precisionValue= precisionValue + newPrecisionValue
            # print("Precision Value at %s:======== %s"%(count+1, precisionValue))
            cutoffValue = cutoffValue + 1
            # print("CutoffValue========%s"%cutoffValue)
            count = count +1


        else:
            # print("inside else===========--------===========")
            count = count +1
    return precisionValue/cutoffValue

# ------Calculating average precision for each data-------------

precisionValueSetosa = avgPrecision("setosa")
print("Average Precision for Setosa:========== %s"%precisionValueSetosa)

precisionValueVersicolor = avgPrecision("versicolor")
print("Average Precision for versicolor:========== %s"%precisionValueVersicolor)

precisionValueVirginica = avgPrecision("virginica")
print("Average Precision for virginica:========== %s"%precisionValueVirginica)

#------------------Calculating the Mean Average Precision------------

MAPValue = (precisionValueSetosa+precisionValueVersicolor+precisionValueVirginica)/3

print("MAP of query 1======%s"%MAPValue)