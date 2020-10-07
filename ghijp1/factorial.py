
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f







n= int(input("hey user eneter number to find a factorial"))
result= fact(n)
print(result)