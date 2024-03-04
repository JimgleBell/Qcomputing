z1 = input()
z2 = input()

z1 = complex(z1)
z2 = complex(z2)


print("|z1|*|z2| = |z1*z2|", (abs(z1)*abs(z2) == abs(z1*z2)))
print("|z1+z2| <= |z1|+|z2|", (abs(z1+z2) <= abs(z1)+abs(z2)))