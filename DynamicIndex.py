import jieba

from index import convert, doc2tokens, dataClean, getStopWords, getDocNum

def getOldTerms():
    old_terms=[]
    with open('dictionary.txt', 'r') as file:
        old_terms=file.read().split('\n')[:-1]
    return(old_terms)

def getOldPostings():
    old_postings=[]
    with open('posting.txt', 'r') as file:
        lines=file.read().split('\n')[:-1]
        for line in lines:
            # strings=line.split(' ')
            # doc_posting=[]
            # for element in strings[0][1:-1].split(', '):
            #     doc_posting.append((int)element)
            # freq_posting=[]
            # for element in strings[1][1:-1].split(','):
            #     freq_posting.append((int)element)
            # old_postings.append([doc_posting, freq_posting)
            strings=line.split('  ')
            doc=[(int)(element) for element in strings[0][1:-1].split(', ')]
            freq=[(int)(element) for element in strings[1][1:-1].split(', ')]
            old_postings.append([doc, freq])
    return old_postings

def mergePosting(posting1, posting2):
    count1=0
    count2=0
    len1=len(posting1[0])
    len2=len(posting2[0])
    # print(posting1)
    # print(posting2)
    p1=[]
    p2=[]
    while(count1!=len1 and count2!=len2):
        if(posting1[0][count1]<posting2[0][count2]):
            p1.append(posting1[0][count1])
            p2.append(posting1[1][count1])
            count1+=1
        elif(posting1[0][count1]==posting2[0][count2]):
            p1.append(posting1[0][count1])
            p2.append(posting1[1][count1]+posting2[1][count2])
            count1+=1
            count2+=1
        else:
            p1.append(posting2[0][count2])
            p2.append(posting2[1][count2])
            count2+=1
    while(count1!=len1):
        p1.append(posting1[0][count1])
        p2.append(posting1[1][count1])
        count1+=1
    while(count2!=len2):
        p1.append(posting2[0][count2])
        p2.append(posting2[1][count2])
        count2+=1
    return [p1, p2]

def merge(oldTerm, oldPosting, newTerm, newPosting):
    mergedList=[]
    count_old=0
    count_new=0
    len_old=len(oldTerm)
    len_new=len(newTerm)
    while count_old!=len_old and count_new!=len_new:
        if oldTerm[count_old]<newTerm[count_new]:
            mergedList.append([oldTerm[count_old], oldPosting[count_old]])
            count_old+=1
        elif oldTerm[count_old]==newTerm[count_new]:
            old=oldPosting[count_old]
            new=newPosting[count_new]
            mergedList.append([oldTerm[count_old], mergePosting(old, new)])
            count_old+=1
            count_new+=1
        else:
            mergedList.append([newTerm[count_new], newPosting[count_new]])
            count_new+=1
    while count_old!=len_old:
        mergedList.append([oldTerm[count_old], oldPosting[count_old]])
        count_old+=1
    while count_new!=len_new:
        mergedList.append([newTerm[count_new], newPosting[count_new]])
        count_new+=1
    return mergedList


new_corpora=convert('new_data_xml.dat')
new_tokens_list=[doc2tokens(doc) for doc in new_corpora]
new_docnum=len(new_corpora)


stopwords=getStopWords()

cleaned_tokens_list=[dataClean(tokens) for tokens in new_tokens_list]
# print(cleaned_tokens_list)

docNum=getDocNum()

new_dictionary=dict()
for i in range(0, len(cleaned_tokens_list)):
    cleaned_tokens=cleaned_tokens_list[i]
    for cleaned_token in cleaned_tokens:
        if(cleaned_token not in new_dictionary.keys()):
            new_dictionary[cleaned_token]=[]
            new_dictionary[cleaned_token].append(i+docNum) # [N doc, total frequency, doc_list, frequency_list]
        else:
            new_dictionary[cleaned_token].append(i+docNum)
# print(new_dictionary.keys())
# print(new_dictionary['月'])

new_terms=sorted(list(new_dictionary.keys()), key=lambda k:k)
# print(new_terms)
new_postingList=[]
for new_term in new_terms:
    docnos=new_dictionary[new_term]
    docno_list=[docnos[0]]
    freq_list=[1]
    count=0
    for i in range(1, len(docnos)):
        if docnos[i]==docnos[i-1]:
            freq_list[count]+=1
        else:
            docno_list.append(docnos[i])
            freq_list.append(1)
    new_postingList.append([docno_list, freq_list])
# print(new_terms[-6]+' '+str(new_postingList[-6]))

old_terms=getOldTerms()
# print(old_terms[10])

old_postings=getOldPostings()
# print(old_postings[0])

mergedPosting=merge(old_terms, old_postings, new_terms, new_postingList)

# print(mergedPosting[0])

# with open('dynamicTerm.txt', 'w') as file:
#     for ele in mergedPosting:
#         file.write(ele[0]+'\n')
# with open('dynamicPosting.txt', 'w') as file:
#     for ele in mergedPosting:
#         file.write(str(ele[1][0])+'  '+str(ele[1][1])+'\n')


# print(mergePosting(old_postings[200], new_postingList[20]))