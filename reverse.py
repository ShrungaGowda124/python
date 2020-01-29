#reverse number

n=int(input("Enter number: "))
reverse=0
while(n>0):
    dig=n%10
    reverse=(reverse*10)+dig
    n=n//10
    print("reverse of the number :",reverse)



'''eg: 4562
    4562>0
    dig=4562%10
    dig=2

    rev=(rev*10)+dig
    rev=(0*10)+2
    n=4562//10
    n=456
    rev=2


    n=456
    dig=6
    rev=6
    n=45
    ...'''
