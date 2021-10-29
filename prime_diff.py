def main():
   testCase = int(input())
   def isprime(n):
       if n<=1:
           return False
       for i in range(2,n):
           if n%i == 0:
               return False
       return True
   while testCase>0:
       LR = list(map(int,input().strip().split()))
       lst=[]
       first = LR[0]
       last = LR[1]
       for i in  range(first,last+1):
           if isprime(i):
               lst.append(i)
               break
           else:
               i=i+1
       for i in range(last,first,-1):
           if isprime(i):
               lst.append(i)
               break
           else:
               i=i+1
       n=len(lst)
       if n>1:
           print(max(lst)-min(lst)
       elif n==1:
           print(0)
       else:
           print(-1)
       testCase -=1
main()
