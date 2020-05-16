from index import InvertedIndex, getLength, getDocNum

tfidfIndex=dict()
length=getLength()

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

# 
idf=[]



if __name__=='__main__':
    print("boolean tfidf")
    # print(length)
    # print(terms.index('总部'))
    # print(getDocNum())