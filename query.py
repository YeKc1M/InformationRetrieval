from index import ANDALL, ORALL, getDocNum, getDocList
from logical import NOT

#string='一个ANDNOT 公司 AND 市场'
string='NOT 未来OR 现在OR 过去'

# s=string.split('AND')
# print(s)
# tokens=[token.strip() for token in s]
# print(tokens)
# tokens.insert(1,'测试')
# print(tokens)

docNum=getDocNum()

def parseADD(string):
    s=string.split('AND')
    unnot_tokens=[token.strip() for token in s]
    l=[]
    for token in unnot_tokens:
        if token.find('NOT')==-1:
            l.append(getDocList(token))
        else:
            token=token.split('NOT')[1]
            token=token.strip()
            l.append(NOT(getDocList(token), docNum))
        print(getDocList(token))
    return ANDALL(l)

def parseOR(string):
    s=string.split('OR')
    unnot_tokens=[token.strip() for token in s]
    l=[]
    for token in unnot_tokens:
        if token.find('NOT')==-1:
            l.append(getDocList(token))
        else:
            token=token.split('NOT')[1]
            token=token.strip()
            l.append(NOT(getDocList(token), docNum))
        print(getDocList(token))
    return ORALL(l)


if __name__=='__main__':
    # print(parseADD(string))
    print(parseOR(string))