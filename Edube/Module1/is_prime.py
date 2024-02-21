def is_prime(num):
    counter = 0
    for i in range(2,num):
        if num % i == 0:
            counter += 1
    return False if (counter > 1) else True
# Escribe tu código aquí.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
