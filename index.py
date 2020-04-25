import jieba

from logical import AND, OR

# news_tensite_xml.smarty.dat
# convert .data to corpora list
def convert(filename):
    l=[]
    with open(filename, 'r', encoding='gbk') as f:
        for line in f:
            # print(line)
            if line.find('<content>')==0:
                # print(line)
                # print(line[9:-11])
                l.append(line[9:-11])
    return l


corpora=convert('news_tensite_xml.smarty.dat')
# print(l)

def doc2tokens(document):
    # print(type(jieba.lcut(document)))
    return jieba.lcut(document)

tokens_list=[doc2tokens(doc) for doc in corpora]
#print(tokens_list[0])

# clean data
stopwords=[]
with open('stopwords.txt', 'r') as f:
    fstr=f.read()
    stopwords=fstr.split('\n')
# print(stopwords)
# print(tokens_list[0][-12] in stopwords)

def dataClean(tokens):
    l=[]
    for token in tokens:
        if(token not in stopwords):
            l.append(token)
    return l

# print(dataClean(tokens_list[0]))
cleaned_tokens_list=[dataClean(tokens) for tokens in tokens_list]
# print(cleaned_tokens_list)
# print(corpora[24])

dictionary=dict()
for i in range(0, len(cleaned_tokens_list)):
    cleaned_tokens=cleaned_tokens_list[i]
    for cleaned_token in cleaned_tokens:
        if(cleaned_token not in dictionary.keys()):
            dictionary[cleaned_token]=[]
            dictionary[cleaned_token].append(i)
        else:
            # if(i not in dictionary[cleaned_token]):
            #     dictionary[cleaned_token].append(i)
            dictionary[cleaned_token].append(i)
# print(dictionary['未来'])
# print(dictionary.keys())

invertedIndex=dict()
for key in dictionary.keys():
    docno_list=dictionary[key]
    totalFreq=len(docno_list)
    invertedIndex[key]=[1, totalFreq,[docno_list[0]],[1]] #[N doc, total frequency, doc_list, frequency_list]
    docCount=1
    for i in range(1, totalFreq):
        # token in same doc
        if(docno_list[i]==docno_list[i-1]):
            invertedIndex[key][3][docCount-1]+=1
        # token not in same doc
        else:
            docCount+=1
            invertedIndex[key][2].append(docno_list[i])
            invertedIndex[key][3].append(1)
    invertedIndex[key][0]=docCount
# print(invertedIndex['未来'])

def InvertedIndex():
    return invertedIndex

def getDocList(token):
    return invertedIndex[token][2]

docNum=len(corpora)
def getDocNum():
    return docNum
# print(getDocList('一个'))

def ANDALL(docno_lists):
    sortedList=sorted(docno_lists, key=lambda k:len(k))
    # print(sortedList)
    res=sortedList[0]
    for i in range(1, len(sortedList)):
        res=AND(res, sortedList[i])
    return res

def ORALL(docno_lists):
    sortedList=sorted(docno_lists, key=lambda k:len(k), reverse=True)
    # print(sortedList)
    res=sortedList[0]
    for i in range(1, len(sortedList)):
        res=OR(res, sortedList[i])
    return res


if __name__=='__main__':
    l1=[2,4,6,7]
    l2=[3,5,7,8]