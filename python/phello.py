lis =[3,12,8,5,66,433,1,33,88]
def sorpot():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] >lis[j+1]:
                lis[j],lis[j+1] =lis[j+1],lis[j]
    print(lis)
    return lis
sorpot()