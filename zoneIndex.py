import jieba

from index import dataClean, getStopWords

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