import chardet
import sys
sys.setrecursionlimit(1000000)
d="[\u4e00-\u9fa5]+"
result=[]
with open('现代汉语常用词表.txt','r') as f:
    for line in f:
        line=line.split()
        result.append(line[0])
list=sorted(result,key=lambda i:len(i),reverse=True)
length=len(list)
l=10
array=[None for j in range(0,11)]
right=0
for i in range(0,length):
    if len(list[i])==l:
        continue
    else:
        array[l]=list[right:i]
        right=i
        l=l-1
array[7].append(array[8][0])
array[1]=list[right:len(list)]
array[8]=None
f=open('liulangdiqiu_liucixin.txt','r')
str=f.read().split()
str="".join(str)


def maxmatch(sentence,dic):
    l=len(sentence)
    if l==0:
        return []
    for i in range(10,0,-1):
        if dic[i] is not None:
            for a in dic[i]:
                if l>=i and a==sentence[0:i]:
                    return [a]+maxmatch(sentence[i:l],dic)
    return maxmatch(sentence[1:l],dic)
s=maxmatch(str,array)
s="   ".join(s)
with open(('test.txt'),'w') as f:
    f.write(s)