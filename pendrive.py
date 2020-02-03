pendrive={540:"sanddish",640:"hp",600:"fp",590:"samsang",480:"filpcant"}
price=0
print(pendrive)

def delete(pos=0):
    price=int(input("enter the price you want to delete: "))
    if pendrive.get(price,"not exist"):
        del pendrive[price]
        print(pendrive)
        pos+=1
        if pos>len(pendrive)-1:
            return
        delete()
    else:
        print("does not exist")
        return
    delete()
delete()