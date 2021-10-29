#program to match the string blood and virus
def main(B,V):
    i=0
    j=0
    while ( i<len(V) and j<len(B)):
        if V[i]==B[j]:
            j=j+1
        i=i+1
    return j==len(B)
V=str(input("Enter virus name : ")).lower()
N=int(input("How many blood sample to check :"))
for l in range(N):
    B=str(input("Enter Blood sample : ")).lower()
    if main(B,V):
         print("POSITIVE")
    else:
         print("NEGATIVE")
