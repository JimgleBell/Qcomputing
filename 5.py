
z1 = complex(input())
z2 = complex(input())
z3 = complex(input())

#A
foo = z1 + z2
bar = z2 + z1
print(foo,bar)

foo = z1*z2
bar = z2*z1
print(foo,bar)

#B
foo = (z1+z2)+z3
bar = z1+(z2+z3)
print(foo,bar)
foo = (z1*z2)*z3 
bar = z1*(z2*z3)
print(foo,bar)

#C
foo = z1*(z2+z3)
bar = (z1*z2)+(z1*z3)
print(foo,bar)
