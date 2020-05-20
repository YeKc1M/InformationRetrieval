from index import InvertedIndex, getLength, getDocNum, dataClean
from test import calculateWf1, calculateWf2
import jieba
import math

length=getLength()
# print(length)

terms=[]
with open('dictionary.txt', 'r') as f:
    file=f.read()
    terms=file.split('\n')[:-1]
# print(terms)
docs=[]
freqs=[]
with open('posting.txt', 'r') as f:
    file=f.read()
    elements=file.split('\n')[:-1]
    posting_str=[element.split('  ') for element in elements]
    # print(posting_str)
    for element in posting_str:
        docs_str=element[0][1:-1].split(', ')
        freqs_str=element[1][1:-1].split(', ')
        # print(docs_str)
        # print(freqs_str)
        docs.append([int(ele) for ele in docs_str])
        freqs.append([int(ele) for ele in freqs_str])
# print(docs)
# print(freqs)

# calculate idf
docNum=getDocNum()
idf=[math.log10(docNum/len(element)) for element in docs]
# print(len(idf))

# calculate tf
tf=[]
for i in range(len(docs)):
    # for terms[i]
    doclist=docs[i]
    freqlist=freqs[i]
    # 
    tflist=[freqlist[j]/length[doclist[j]] for j in range(len(doclist))]
    # print(tflist)
    tf.append(tflist)
# print(tf)
# print(len(tf))

# calculate tfidf
tfidf=[]
for i in range(len(idf)):
    # for terms[i]
    tflist=tf[i]
    element=[idf[i]*tflist[j] for j in range(len(tflist))]
    # print(element)
    tfidf.append(element)
# print(tfidf)
# print(len(tfidf))

def getTfidf(token):
    if token not in terms:
        return []
    return tfidf[terms.index(token)]
def getDocs(token):
    if token not in terms:
        return []
    return docs[terms.index(token)]
def getPosting(token):
    return [getDocs(token), getTfidf(token)]
# print(getTfidf('月'))
# token='月'
# print(len(getDocs(token))==len(getTfidf(token)))
# print(getPosting(token))

# calculate wfidf1
# wf1=1+log(tf)
wfidf1=[]
# print(tf)
for i in range(len(tf)):
    # for terms[i]
    i_tf=tf[i]
    i_idf=idf[i]
    wfidf1.append([calculateWf1(element)*i_idf for element in i_tf])
# print(wfidf1)
# for element in wfidf1:
#     for ele in element:
#         if(ele<=0):
#             print(ele)
# print(len(wfidf1[0]))
# print(tfidf[0])
def getWfidf1(token):
    if token in terms:
        return wfidf1[terms.index(token)]
    return []
# print(getWfidf1('月'))
def getWfidfPosting1(token):
    return [getDocs(token), getWfidf1(token)]
# print(getWfidfPosting1('一个'))

#calculate wfidf2
wfidf2=[]
for i in range(len(tf)):
    i_tf=tf[i]
    i_idf=idf[i]
    wfidf2.append([calculateWf2(element, i_tf)*i_idf for element in i_tf])
# print(wfidf2[0])
# print(len(wfidf2[0]))
def getWfidf2(token):
    if token in terms:
        return wfidf2[terms.index(token)]
    return []
def getWfidfPosting2(token):
    return [getDocs(token), getWfidf2(token)]
# print(getWfidfPosting2('一个'))

def postingOR(posting1, posting2):
    count1=0
    count2=0
    length1=len(posting1[0])
    length2=len(posting2[0])
    # print(length1)
    # print(length2)
    res=[]
    while count1!=length1 and count2!=length2:
        if posting1[0][count1]<posting2[0][count2]:
            res.append([posting1[0][count1], posting1[1][count1]])
            count1+=1
        elif posting1[0][count1]==posting2[0][count2]:
            res.append([posting1[0][count1], posting1[1][count1]+posting2[1][count2]])
            count1+=1
            count2+=1
        else:
            res.append([posting2[0][count2], posting2[1][count2]])
            count2+=1
    while count1!=length1:
        res.append([posting1[0][count1], posting1[1][count1]])
        count1+=1
    while count2!=length2:
        res.append([posting2[0][count2], posting2[1][count2]])
        count2+=1
    p1=[]
    p2=[]
    for i in range(len(res)):
        p1.append(res[i][0])
        p2.append(res[i][1])
    return [p1, p2]
# print(getPosting('一个'))
# print(getPosting('学校'))
# print(postingOR(getPosting('一个'), getPosting('学校')))

def ORALL(sortedPostings):
    if len(sortedPostings)==0:
        return [[],[]]
    res=sortedPostings[0]
    for i in range(1, len(sortedPostings)):
        res=postingOR(res, sortedPostings[i])
    l=[]
    for i in range(len(res[0])):
        l.append([res[0][i], res[1][i]])
    return l

def tfidfSearch(query):
    jiebalcut=jieba.lcut(query)
    tokens=dataClean(jiebalcut)
    # print(tokens)
    postings=[getPosting(element) for element in tokens]
    # print(postings)
    postings=sorted(postings, key=lambda k: len(k[0]))
    print(postings)
    return ORALL(postings)

def wfidfSearch1(query):
    jiebalcut=jieba.lcut(query)
    tokens=dataClean(jiebalcut)
    postings=[getWfidfPosting1(element) for element in tokens]
    postings=sorted(postings, key=lambda k: len(k[0]))
    print(postings)
    return ORALL(postings)

def wfidfSearch2(query):
    jiebalcut=jieba.lcut(query)
    tokens=dataClean(jiebalcut)
    postings=[getWfidfPosting2(element) for element in tokens]
    # print(postings)
    postings=sorted(postings, key=lambda k: len(k[0]))
    print(postings)
    return ORALL(postings)

# print(tfidf[terms.index('月')])
# print(tfidfSearch('一个中国梦'))
# print(wfidfSearch1('一个中国'))
# print(wfidfSearch2('一个中国'))

if __name__=='__main__':
    print("boolean tfidf")
    # print(length)
    # print(terms.index('总部'))
    # print(getDocNum())