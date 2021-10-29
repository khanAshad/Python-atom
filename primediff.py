#program to print difference between two prime (one smallest and other largest prime number in given range )
def findprime(N):
    flag=True
    if N>1:
        for k in range (2,N):
            if N%k==0:
                flag=False
                break
    return flag
def mainf(L,R):
    sp=0
    bp=0
    for i in range (L,R+1):
        if findprime(i):
            sp=i
            break
    for j in range (R,L-1,-1):
        if findprime(j):
            bp=j
            break
    if sp==0 and bp==0:
        print("-1")
    elif sp!=0 and bp!=0:
        print(bp-sp)
    else:
        print("0")
T=int(input())
for l in range(T):
    num=list(input().split())
    L=int(num[0])
    R=int(num[1])
    mainf(L,R)
