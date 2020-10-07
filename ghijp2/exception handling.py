a=int(input("hey enter a number"))
b=int(input("hey enter b number"))

try:
    print("resource open")
    print(a/b)
    z=int(input("enter dupe value"))
    print(z)
except ZeroDivisionError as e:
    print("number cannot divided by zero",e)
except ValueError as e:
    print("invalid value",e)
except Exception as e:
    print("something went wrong...",e)
finally:
    print("resource closed")