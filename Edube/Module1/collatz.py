number = int(input("Give me an number: "))
steps = 0

while number != 1:
    if (number % 2): #This means number % 2 != 0 equals True. Only a result of zero will be considered False
        number = int((number * 3 ) + 1)
        print (number,end=", ")
    else:
        number /= 2
        print(int(number),end=", ")
    steps += 1
print()
message = f"Number of steps: {steps}"
if steps < 10:
    print (message)
else: 
    message = f"¡La madre que te parió: {message}!"
    print (message)
    