import jieba

from index import convert, doc2tokens, dataClean, getStopWords

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

new_corpora=convert('new_data_xml.dat')
new_tokens_list=[doc2tokens(doc) for doc in new_corpora]
new_docnum=len(new_corpora)


stopwords=getStopWords()

cleaned_tokens_list=[dataClean(tokens) for tokens in new_tokens_list]
# print(cleaned_tokens_list)

new_dictionary=dict()
for i in range(0, len(cleaned_tokens_list)):
    cleaned_tokens=cleaned_tokens_list[i]
    for cleaned_token in cleaned_tokens:
        if(cleaned_token not in new_dictionary.keys()):
            new_dictionary[cleaned_token]=[]
            new_dictionary[cleaned_token].append(i) # [N doc, total frequency, doc_list, frequency_list]
        else:
            new_dictionary[cleaned_token].append(i)
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
