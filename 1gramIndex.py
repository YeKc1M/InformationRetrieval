import jieba

from logical import AND, OR, NOT, ANDNOT, ORNOT

def getTerms():
    old_terms=[]
    with open('dictionary.txt', 'r') as file:
        old_terms=file.read().split('\n')[:-1]
    return(old_terms)

terms=getTerms()

index=dict()
for term in terms:
    for i in range(0, len(term)):
        if term[i] in index.keys():
            if term not in index[term[i]]:
                index[term[i]].append(term)
        else:
            index[term[i]]=[term]
# print(index.keys())
# print(len(index.keys()))
# print(index['超'])

print(index['个'])
print(index['人'])
print(AND(index['个'],index['人']))