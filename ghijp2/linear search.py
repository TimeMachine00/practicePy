pos=-1
def search (list,n):
    i=0
    while i <len(list):
        if list[i]==n:
            globals() ['pos']=i
            return True
        i=i+1

    return  False
list =[5,4,6,7,8,9,3,2,1]
n=int(input("hey enter n"))
if search(list,n):
    print("found at ", pos+1)
else:
    print("not found n")