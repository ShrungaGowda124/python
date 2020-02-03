def binary(num):
    if num>1:
        binary(num//2)
    print(num%2,end="")
if __name__=="__main__":
    print()
    binary(11)