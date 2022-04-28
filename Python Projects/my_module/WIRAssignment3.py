import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("newDataCsv.csv")
documents = df["document"]

print(df)

count = 0
relevantCount = 0

precision = []
recall = []
pSum = 0
rSum = 0
gs = 15

# Precision and recall of first 10 instances of documents
while count < documents.count():
    currentdf = df.iloc[count]
    print(currentdf["status"])

    status = currentdf["status"]

    if status == "relevant":
        relevantCount = relevantCount + 1
        precisionValue = relevantCount/(count+1)
        recallValue = relevantCount / gs

    else:
        precisionValue = relevantCount / (count+1)
        recallValue = relevantCount / gs

    count = count + 1

    precision.append(round(precisionValue,2))
    pSum = pSum + precisionValue
    recall.append(round(recallValue,2))
    rSum = rSum + recallValue


print(precision)
print(round(pSum,2))
print(recall)
print(round(rSum,2))


# F1 score at last instance

finalRelevant = df[df["status"] == "relevant"].count()
finalNotRelevant = df[df["status"] == "not relevant"].count()
totalRetreived = df["document"].count()

finalPrecision = finalRelevant / totalRetreived
finalRecall = finalRelevant / gs

f1Score = (2 * finalPrecision * finalRecall) / (finalPrecision + finalRecall)

print(f1Score["document"])

# Graph of precision and recall values
rank = range(len(precision))
plt.plot(rank, precision)
plt.plot(rank, recall)
plt.show()

#
plt.plot(recall,precision,'b')
plt.title("recall and Precision values where N=50")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()