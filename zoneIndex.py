import jieba

from index import dataClean, getStopWords, getDocList, InvertedIndex

titles=[]
with open('news_tensite_xml.smarty.dat','r', encoding='gbk') as file:
    for line in file:
        if line.find('<contenttitle>')==0:
            titles.append(line[14:-16])
# print(titles)

title_tokens_list=[jieba.lcut(title) for title in titles]
# print(title_tokens_list)
stopwords=getStopWords()
# print(stopwords)
cleaned_title_tokens_list=[dataClean(element) for element in title_tokens_list]
# print(cleaned_title_tokens_list)

zoneIndex=dict()
for i in range(0, len(cleaned_title_tokens_list)):
    element=cleaned_title_tokens_list[i]
    for token in element:
        if token in zoneIndex.keys():
            if i not in zoneIndex[token]:
                zoneIndex[token].append(i)
        else:
            zoneIndex[token]=[i]
# for key in zoneIndex.keys():
#     print(key+' '+str(zoneIndex[key]))
# print(zoneIndex.keys())
# print(zoneIndex['非法'])

weight={'title':0.6, 'content':0.4}

def singleWeight(token):
    res=[]
    if token not in zoneIndex.keys():
        titlenos=[]
    else:
        titlenos=zoneIndex[token]
    contentnos=getDocList(token)
    countt=0
    countc=0
    lent=len(titlenos)
    lenc=len(contentnos)
    # print(titlenos)
    # print(contentnos)
    while countt!=lent and countc!=lenc:
        if titlenos[countt]<contentnos[countc]:
            res.append([titlenos[countt], weight['title']])
            countt+=1
        elif titlenos[countt]==contentnos[countc]:
            res.append([titlenos[countt], weight['title']+weight['content']])
            countt+=1
            countc+=1
        else:
            res.append([contentnos[countc],weight['content']])
            countc+=1
    while countt!=lent:
        res.append([titlenos[countt], weight['title']])
        countt+=1
    while countc!=lenc:
        res.append([contentnos[countc], weight['content']])
        countc+=1
    return res

invertedIndex=InvertedIndex()

def postingADD(posting1, posting2):
    count1=0
    count2=0
    len1=len(posting1)
    len2=len(posting2)
    res=[]
    while count1!=len1 and count2!=len2:
        if posting1[count1][0]<posting2[count2][0]:
            count1+=1
        elif posting1[count1][0]==posting2[count2][0]:
            res.append([posting1[count1][0], posting1[count1][1]+posting2[count2][1]])
            count1+=1
            count2+=1
        else:
            count2+=1
    return res

def weightADD(string):
    tokens=jieba.lcut(string)
    cleaned=dataClean(tokens)
    posting=[singleWeight(token) for token in cleaned]
    posting=sorted(posting, key=lambda k: len(k))
    # print(posting)
    res=posting[0]
    for i in range(1, len(posting)):
        res=postingADD(res, posting[i])
    return sorted(res, key=lambda k: k[1], reverse=True)

def simpleADD(string):
    tokens=jieba.lcut(string)
    # print(tokens)
    cleaned=dataClean(tokens)
    # print(cleaned)
    doc_lists=[invertedIndex[element][2] for element in cleaned]
    # doc_lists=[getDocList(element) for element in cleaned]
    freq_lists=[invertedIndex[element][3] for element in cleaned]
    # print(doc_lists)
    # print(freq_lists)
    posting=[]
    for i in range(len(doc_lists)):
        element=[]
        doc_list=doc_lists[i]
        freq_list=freq_lists[i]
        for j in range(len(doc_list)):
            element.append([doc_list[j],freq_list[j]])
        posting.append(element)
    # print(posting)
    posting=sorted(posting, key=lambda k:len(k))
    # print(posting)
    res=posting[0]
    for i in range(1, len(posting)):
        res=postingADD(res, posting[i])
    return sorted(res, key=lambda k: k[1], reverse=True)


string='现在一个'
# print(simpleADD(string))
# print(singleWeight('现在'))
# print(weightADD(string))