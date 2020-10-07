def top10():
    n=1
    while n<=10:
        sqr=n*n
        yield sqr
        n+=1

values=top10()
for i in values:
    print(i)