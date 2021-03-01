import string

alphaList= list(string.ascii_lowercase)
print(alphaList)

def shiftleft(str):
    res = []
    for ch in str:
        index = alphaList.index(ch)
        index -= 1
        res.append(alphaList[index])
    return ''.join(res)
def shiftright(str):
    res = []
    for ch in str:
        index = alphaList.index(ch)
        if index == len(alphaList) - 1:
            index = 0
        else:
            index += 1
        res.append(alphaList[index])
    return ''.join(res)

print(shiftright("abc"))