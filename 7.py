# Insert the numbers in the format (a+bj)

str1 = input() 
str2 = input() 

z1 = complex(str1)
z2 = complex(str2)

print("conj(z1)+conj(z2) = conj(z1+z2)", (z1.conjugate()+z2.conjugate() == (z1+z2).conjugate()))
print("conj(z1)*conj(z2) = conj(z1*z2)", (z1.conjugate()*z2.conjugate() == (z1*z2).conjugate()))