def checkPrime(n):
    if n<=1:
        return False
    for e in range (2,n):
        if(n % e ==0):
            return False
    return True
counter=0
n=2
f=open("prime.txt","w")
while counter<10000:
    if checkPrime(n):
        f.write("%d\n" % n)
        counter=counter+1
    n=n+1
print("Done")
f.close()

'''Run time take a while!!!'''