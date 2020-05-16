import math

# calculate wfidf
def calculateWf(num):
    if num==0:
        return 0
    else:
        return math.log(num, 10)

def wfidf():
    idf=[1.65, 2.08, 1.62, 1.5]
    tf1=[[27,3,0,14],[4,33,33,0],[24,0,29,17]]
    tf2=[[0.88,0.1,0,0.46],[0.09,0.71,0.71,0],[0.58,0,0.7,0.41]]
    wfidf1=[]
    wfidf2=[]
    for element in tf1:
        l=[]
        for i in range(len(idf)):
            l.append(idf[i]*calculateWf(element[i]))
        wfidf1.append(l)
    print(wfidf1)
    for element in tf2:
        l=[]
        for i in range(len(idf)):
            l.append(idf[i]*calculateWf(element[i]))
        wfidf2.append(l)
    print(wfidf2)

if __name__=='__main__':
    print("test.py")
    # print(calculateWf(0))
    # print(calculateWf(10))
    wfidf()