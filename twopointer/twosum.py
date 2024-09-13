import itertools
from collections import defaultdict
def brute(a,tar):
    allpairs=[]
    count=0
    for i in range(len(a)-1):
        for j in range(i+1,len(range(len(a)))):
            if a[i]+a[j]==tar:
                count+=1
                lst=[]
                lst.extend([a[i],a[j]])
                allpairs.append(lst)
    print('all pairs are ',allpairs)
    print("count of all pairs are ",count)
    l=list( allpairs for allpairs,_ in itertools.groupby(allpairs))
    print('uniqu pairs are',l)
    print('brute over')




def twoptr(a,tar):
    start=0
    end=len(a)-1
    tcnt=0
    while(start<=end):
        if a[start]+a[end]<tar:
            start+=1
        elif a[start]+a[end]>tar:
            end-=1
        else:
            if a[start]!=a[end]:
                scnt=1
                while(a[start]==a[start+1]):
                    scnt+=1
                    start+=1
                start+=1
                ecnt=1
                while(a[end]==a[end-1]):
                    ecnt+=1
                    end-=1
                end-=1
                cnt=scnt*ecnt
                tcnt=tcnt+cnt
            else:
                fcnt=1
                while(a[start]==a[start+1]):
                    fcnt+=1
                    start+=1
                
                start+=1
                tcnt=tcnt+int((fcnt*(fcnt-1)/2))
    print(tcnt)
a=[1,1,2,2,2,3,4,5,5,5,6,7,8,8,9]
brute(a,5)
twoptr(a,5)

