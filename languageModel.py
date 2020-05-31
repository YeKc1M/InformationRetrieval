import jieba
from index import getLength, dataClean, getCorpora
from booleanTfidf import Terms
from vectortfidf import getVectorTf

terms=Terms()
# print(terms)
vectorTf=getVectorTf() # index indicating docNo. containing token occurances of term in i_th document
# print(vectorTf[0])
length=getLength() # token number of i_th document

Mc=[] # index indicating termNo. containing i_th token occurances of term in the collection
for i in range(len(terms)):
    Mc.append(0)
totalNum=0 # total number of tokens in the collection
for element in vectorTf:
    for ele in element:
        Mc[ele[0]]+=ele[1]
        totalNum+=ele[1]
# print(totalNum)
# print(Mc[0])
# print(totalNum==sum(length))

Md=[] # containing i_th document [terms, occurances]. terms containing termNo 
for element in vectorTf:
    termlist=[]
    occurlist=[]
    for ele in element:
        termlist.append(ele[0])
        occurlist.append(ele[1])
    Md.append([termlist, occurlist])
# print(len(Md))
# print(len(Md[0][0])==len(vectorTf[0]))
# print(Md[0])

weight=[0.9, 0.1] # 0-Md, 1-Mc

def cal_term_pro_Md(term):
    termNo=-1
    res=[]
    try:
        termNo=terms.index(term)
        for i in range(len(Md)):
            element=Md[i]
            if termNo in element[0]:
                res.append(element[1][element[0].index(termNo)]/length[i])
            else:
                if len(element[1])==0:
                    res.append(0)
                else:
                    res.append(min(element[1])*0.00001/length[i])
    except ValueError:
        termNo=-1
        for i in range(len(Md)):
            res.append(0.000000001)
    # print(len(res))
    return res

# cal_term_pro_Md('一个')
# print(cal_term_pro_Md('一个').index(max(cal_term_pro_Md('一个'))))
# print(getCorpora()[126])

def cal_term_pro_Mc(term):
    termNo=-1
    res=0
    try:
        termNo=terms.index(term)
        res=Mc[termNo]/totalNum
    except ValueError:
        res=min(Mc)*0.001/totalNum
    # print(termNo)
    return res
# print(cal_term_pro_Mc('一个个个'))
# print(terms.index('龙门山'))
def cal_term_pro(term):
    pro_Mc=cal_term_pro_Mc(term)
    pro_Md=cal_term_pro_Md(term)
    # print(pro_Mc)
    # print(pro_Md)
    # print(len(pro_Md))
    return [weight[0]*element+weight[1]*pro_Mc for element in pro_Md]

# print(cal_term_pro('一个'))

def cal_pro(query):
    l=jieba.lcut(query)
    tokens=dataClean(l)
    # print(tokens)
    pro=[0]*len(Md)
    # print(pro)
    if len(tokens)!=0:
        pro=cal_term_pro(tokens[0])
        for i in range(1, len(tokens)):
            new=cal_term_pro(tokens[i])
            for j in range(len(Md)):
                pro[j]*=new[j]
    res=[]
    # print(len(Md))
    for i in range(len(pro)):
        res.append([i, pro[i]])
    return res

# cal_pro('高考成绩发布')
# print(sorted(cal_pro('日本东京'), key=lambda k:k[1], reverse=True))
# print(getCorpora()[76])