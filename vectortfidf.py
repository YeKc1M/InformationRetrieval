from index import InvertedIndex, getLength, getDocNum, dataClean
from booleanTfidf import Docs, Freqs, Terms, Idf, BooleanTfidf
import jieba
from test import calculateWf2
import math

length=getLength()
# print(length)

terms=Terms()
# print(terms)
docs=Docs()
# print(docs)
freqs=Freqs()
# print(freqs)

docNum=getDocNum()
# print(docNum)
vectorTf=[]
for i in range(docNum):
    vectorTf.append([])
# print(vectorTf)
# print(len(vectorTf))

for i in range(len(terms)):
    # for terms[i]
    doc=docs[i]
    freq=freqs[i]
    for j in range(len(doc)):
        docindex=doc[j]
        freqindex=freq[j]
        vectorTf[doc[j]].append([i, freq[j]])
# print(len(vectorTf[0]))
# print(vectorTf[0])

idf=Idf() # i corresponding to i_th term
# print(idf)
# print(len(idf))

vectorTfidf=[]
for i in range(docNum):
    vectorTfidf.append([])
for i in range(len(vectorTf)):
    # for document i
    for j in range(len(vectorTf[i])):
        # for [term_id, freq]
        term_id=vectorTf[i][j][0]
        vectorTfidf[i].append([term_id, vectorTf[i][j][1]*idf[term_id]])
# print(vectorTfidf[0])
# print(len(vectorTf[11])==len(vectorTfidf[11]))

vectorWfidf1=[]
for i in range(docNum):
    vectorWfidf1.append([])

def calculateWf1(tf):
    if tf==0:
        return 0
    else:
        return 1+math.log(tf, 10)
for i in range(len(vectorTf)):
    # for document i
    for j in range(len(vectorTf[i])):
        # for [term_id, freq]
        term_id=vectorTf[i][j][0]
        vectorWfidf1[i].append([term_id, calculateWf1(vectorTf[i][j][1])*idf[term_id]])
# print(vectorWfidf1[0])
# print(len(vectorTf[100])==len(vectorWfidf1[100]))

vectorWfidf2=[]
for i in range(docNum):
    vectorWfidf2.append([])
for i in range(len(vectorTf)):
    # for document i
    for j in range(len(vectorTf[i])):
        term_id=vectorTf[i][j][0]
        vectorWfidf2[i].append([term_id, calculateWf2(vectorTf[i][j][1], [element[1] for element in vectorTf[i]])*idf[term_id]])
# print(vectorWfidf2[0])
# print(len(vectorTf[11])==len(vectorWfidf2[11]))

stopwords=[]
with open('stopwords.txt', 'r') as f:
    fstr=f.read()
    stopwords=fstr.split('\n')


def dataClean(tokens):
    l=[]
    for token in tokens:
        if(token not in stopwords):
            l.append(token)
    return l

def query2vec(query):
    tokens=jieba.lcut(query)
    cleaned_tokens=dataClean(tokens)
    print(cleaned_tokens)
    querytf=[[terms.index(element), 1] for element in cleaned_tokens if element in terms]
    return sorted(querytf, key=lambda k: k[0])


def sim(vector1, vector2):
    length1=0
    length2=0
    for element in vector1:
        length1+=element[1]**2
    for element in vector2:
        length2+=element[1]**2
    length1=math.sqrt(length1)
    length2=math.sqrt(length2)
    for element in vector1:
        element[1]=element[1]/length1
    for element in vector2:
        element[1]=element[1]/length2
    count1=0
    count2=0
    res=0
    while count1!=len(vector1) and count2!=len(vector2):
        if vector1[count1][0]<vector2[count2][0]:
            count1+=1
        elif vector1[count1][0]==vector2[count2][0]:
            res+=vector1[count1][1]*vector2[count2][1]
            count1+=1
            count2+=1
        else:
            count2+=1
    return res
    
def tfidfsims(query):
    vector=query2vec(query)
    print(vector)
    vectorDocs=[element[0] for element in vector]
    scores=[]
    for i in range(0, len(vectorTfidf)):
        scores.append(0)
    # print(scores)
    for element in vector:
        # for document containing element
        d=docs[element[0]]
        # print(d)
        for ele in d:
            # for docno in d
            for e in vectorTfidf[ele]:
                # for [term_no, tfidf] in vectorTfidf
                if e[0] in vectorDocs:
                    scores[ele]+=e[1]
    for i in range(len(scores)):
        if scores[i]!=0:
            length=0
            for element in vectorTfidf[i]:
                length+=(element[1]**2)
            length=math.sqrt(length)
            scores[i]/=length
    return scores

def wfidf1sims(query):
    vector=query2vec(query)
    print(vector)
    vectorDocs=[element[0] for element in vector]
    scores=[]
    for i in range(0, len(vectorWfidf1)):
        scores.append(0)
    # print(scores)
    for element in vector:
        # for document containing element
        d=docs[element[0]]
        # print(d)
        for ele in d:
            # for docno in d
            for e in vectorWfidf1[ele]:
                # for [term_no, tfidf] in vectorTfidf
                if e[0] in vectorDocs:
                    scores[ele]+=e[1]
    for i in range(len(scores)):
        if scores[i]!=0:
            length=0
            for element in vectorWfidf1[i]:
                length+=(element[1]**2)
            length=math.sqrt(length)
            scores[i]/=length
    return scores

def wfidf2sims(query):
    vector=query2vec(query)
    print(vector)
    vectorDocs=[element[0] for element in vector]
    scores=[]
    for i in range(0, len(vectorWfidf2)):
        scores.append(0)
    # print(scores)
    for element in vector:
        # for document containing element
        d=docs[element[0]]
        # print(d)
        for ele in d:
            # for docno in d
            for e in vectorWfidf2[ele]:
                # for [term_no, tfidf] in vectorTfidf
                if e[0] in vectorDocs:
                    scores[ele]+=e[1]
    for i in range(len(scores)):
        if scores[i]!=0:
            length=0
            for element in vectorWfidf2[i]:
                length+=(element[1]**2)
            length=math.sqrt(length)
            scores[i]/=length
    return scores

def vectortfidfSearch(query):
    vector=query2vec(query)
    # print(vector)
    res=[]
    for i in range(len(vectorTfidf)):
        res.append([i, sim(vectorTfidf[i], vector)])
    return res

def vectorwfidfSearch1(query):
    vector=query2vec(query)
    res=[]
    for i in range(len(vectorWfidf1)):
        res.append([i, sim(vectorWfidf1[i], vector)])
    return res

def vectorwfidfSearch2(query):
    vector=query2vec(query)
    res=[]
    for i in range(len(vectorWfidf2)):
        res.append([i, sim(vectorWfidf2[i], vector)])
    return res
# q='一个中国原则美国'
# for i in range(200):
#     print(str(i)+' '+str(sim(vectorTfidf[i], query2vec(q))))
# print(tfidfsims('中国美国大豆市场'))
# print(wfidf1sims('中国美国大豆市场'))
# print(tfidfsims('中国美国大豆市场'))

if __name__=='__main__':
    query='一个中国原则美国月'
    # print(query2vec(query))
    # print(sim(vectorTfidf[0], query2vec(query)))
    # print(tfidfSearch(query))
    # print(wfidfSearch1(query))
    # print(wfidfSearch2(query))