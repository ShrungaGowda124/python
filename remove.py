def remove(str,start,num):
    string3=""
    string1=list(str)
    for yet in range(0,num):
        for each in range(0,len(str)):
            if each==start:
                del string1[each]
                break
        for i in string1:
            string3+=i
        print(string3)
string2=input("enter the strnig:")
number=int(input("enter the number of characters you wish to remove:"))
begin=int(input("enter the starting point:"))
remove(string2,begin,number)
        
