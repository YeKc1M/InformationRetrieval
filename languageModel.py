import jieba
from index import getLength
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

weight=[0.3, 0.7] # 0-Md, 1-Mc

def cal_term_pro_Md(term):
    termNo=0
    res=[]
    try:
        termNo=terms.index(term)
    except ValueError:
        termNo=-1

cal_term_pro_Md('一个')
# print(terms.index('龙门山'))
# def cal_term_pro(term):
#     proMd=cal_term_pro_Md(term)