#2. Bank chargings
count=0
amount=int(input("enter the amount in your accounts:"))
for yet in range(1,11):
    decide=input("tell us what you wish to do:")
    if decide=="deposit":
        money=int(input("tell us money you wish to deposit:"))
        amount+=money
        print("amount in your account after transaction:",amount)
    elif decide=="withdraw":
        money=int(input("tell us money you wish to withdraw:"))
        if count<5:
            amount-=money
            print("amount in your account after transaction:",amount)
        else:
            amount-=money+20
            print("amount in your account after transaction:",amount)
        count+=1
