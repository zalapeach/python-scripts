# expected output
# x = 1,   y =  0.6000000000000001
# x = 10,  y =  0.09901951266867294
# x = 100, y =  0.009999000199950014
# x = -5,  y = -0.19258202567760344

x = float(input("Gime me the value of x: "))
y = 1/(x + 1/(x + 1/(x + 1/x)))
print("The result is:", y)
