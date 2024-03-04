# Inspecting the powers of i

x = int(input())

if (x % 4 == 0) :
    print(1)
elif(x % 4 == 3) :
    print("-i")
elif(x % 4 == 2) :
    print(-1)
elif(x % 4 == 1) :
    print("i")