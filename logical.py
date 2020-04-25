
def AND(l1, l2):
    l=[]
    c1=0
    c2=2
    length1=len(l1)
    length2=len(l2)
    while(c1!=length1 and c2!=length2):
        if l1[c1]<l2[c2]:
            c1+=1
        elif l1[c1]==l2[c2]:
            l.append(l1[c1])
            c1+=1
            c2+=1
        else:
            c2+=1
    return l

def OR(l1, l2):
    l=[]
    c1=0
    c2=0
    length1=len(l1)
    length2=len(l2)
    while(c1!=length1 and c2!=length2):
        if l1[c1]<l2[c2]:
            l.append(l1[c1])
            c1+=1
        elif l1[c1]==l2[c2]:
            l.append(l1[c1])
            c1+=1
            c2+=1
        else:
            l.append(l2[c2])
            c2+=1
    while(c1!=len(l1)):
        l.append(l1[c1])
        c1+=1
    while(c2!=len(l2)):
        l.append(l2[c2])
        c2+=1
    return l

def ANDNOT(l1, l2):
    l=[]
    c1=0
    c2=0
    length1=len(l1)
    length2=len(l2)
    while(c1!=length1 and c2!=length2):
        if(l1[c1]<l2[c2]):
            l.append(l1[c1])
            c1+=1
        elif(l1[c1]==l2[c2]):
            c1+=1
            c2+=2
        else:
            c2+=1
    return l

# suppose doc no starts with 0
def ORNOT(l1, l2, doc_num):
    l=[]
    c1=0
    c2=0
    length1=len(l1)
    length2=len(l2)
    for i in range(0, doc_num):
        if(c2!=length2):
            if(l2[c2]==i):
                c2+=1
            else:
                l.append(i)
        else:
            l.append(i)
        if(c1!=length1):
            if(l1[c1]==i):
                if(l1[c1]==l2[c2-1]):
                    l.append(i)
                c1+=1
    return l
    
def NOT(l1, doc_num):
    l=[]
    for i in range(0, doc_num):
        if(i not in l1):
            l.append(i)
    return l        


if __name__=='__main__':
    print('logical.py')
    l1=[2,4,6,7]
    l2=[3,5,7,8]
    print(AND(l1,l2))
    print(OR(l1,l2))
    print(NOT(l2, 10))
    print(ANDNOT(l1,l2))
    print(ORNOT(l1, l2, 10))