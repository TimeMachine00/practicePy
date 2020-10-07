pos=-1

def search (list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid =(l+u)//2
        if list[mid]==n:
            globals() ['pos']=mid
            return  True
        else:
            if list[mid]<n:
                l=mid+l
    return False
list =[1,2,3,4,5,6,6,7,8,9,10,12,34,55]
#n=9
n=int(input("hey enter n"))
if search(list,n):
    print("found at ", pos+1)
else:
    print("not found")