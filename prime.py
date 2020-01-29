#prime numbers

n=int(input("enter the initial point: "))
term=int(input("enter the number of terms: "))

prime=[]
for a in range(n,10000):
    for b in range(2,a):
        if(a%b==0):
            break
    else:
        prime.append(a)
    if len(prime)==term:
        break
print("prime numbers are:",prime[:])
