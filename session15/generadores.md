# Generadores

Manera habitual:

```
lista1 = list(range(4))
print(len(lista1))
```

```
sumatorio = 0
```

Todos los nºs se cargarán en memoria para poder ser sumados:

```
for numero in lista1:
    sumatorio += numero
```

Se puede evitar con los generadores:

```
def obtener_datos_lazy():
    for numero in lista1:
        yield numero 

generador = obtener_datos_lazy()
try:
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
except StopIteration:
    print("Sin mas datos")

print("_" * 50)
```

Por cada next, obtengo un nº nuevo de la lista:

```
print(next(generador))
print(next(generador))
print(next(generador))
```

##### Cada next recuerda dónde me he quedado en la secuencia

```
print("-"*70)
for n in generador:
    print(n)
```

El final de next lanza una excepción llamada StopIteration:

```
def generar_datos():
    yield 'A'
    yield from [1,2,3]

generadorv2 = generar_datos()
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())
print(generadorv2.__next__())

print([i*2 for i in  [1,2,3,4,5,6]])
```

##### Equivalente a lo anterior con generadores

```
data = (i*2 for i in [1,2,3,4,5,6])

for item in (i*2 for i in  [1,2,3,4,5,6]):
    print(item)
```

**No se ha cargado todo en memoria**. Sólo los elementos a los que voy accediendo.
print(next(data)) #Da un StopIteration porque los datos a los que se acceden se pierden.

#### Aclaraciones de Copilot

##### User

Is it possible to use the map() function in python without the lambda function?

##### Copilot

Certainly! You can use the map() function in Python without using a lambda function. Instead, you can pass a custom function as the first argument to map(). Here's an example:

```
# Define a custom function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each element in the list
squared_numbers = map(square, numbers)

# Convert the result to a list
squared_numbers_list = list(squared_numbers)

# Print the squared numbers
print(squared_numbers_list)
```

The output will be:

> [1, 4, 9, 16, 25]

In this example, we used the square() function instead of a lambda function to square each element in the numbers list. You can replace square() with any other custom function that you'd like to apply to the elements in your list. 😊🐍

##### User

Is it possible to modify the example using the function yield?

##### Copilot

Certainly! You can modify the example to use the yield keyword instead of returning a list. The yield keyword allows you to create a generator function, which produces values lazily one at a time. Here's an updated version of the example using yield:

##### Define a custom generator function to square numbers

```
def square_generator(numbers):
    for num in numbers:
        yield num ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the square_generator to get squared numbers one at a time
squared_numbers_gen = square_generator(numbers)

# Print the squared numbers
for squared_num in squared_numbers_gen:
    print(squared_num)
```

The output will be the same as before:

> 1
> 4
> 9
> 16
> 25

In this modified example, the square_generator() function uses yield to produce squared numbers lazily as you iterate over them. This approach is memory-efficient because it doesn't create a large list in memory; instead, it generates values on-the-fly. 😊🐍

##### User

Is it correct to say that yield is some kind of return that doesn't make the subrutine in where it is used, stop and also doesn't store every element created in memoryl?

##### Copilot

Yes, that's a spot-on description of the yield keyword in Python! Let me elaborate further:

- yield as a Lazy Generator:
  - When you use yield in a function, it transforms that function into a generator.
  - Unlike a regular function that computes and returns a value immediately, a generator function produces values lazily, one at a time.
  - It doesn't compute all the values upfront and store them in memory; instead, it generates each value on-the-fly as you iterate over it.
  - This makes it memory-efficient, especially when dealing with large data sets or infinite sequences.
- How yield Works:
  - When a generator function is called, it doesn't execute the entire function body immediately.
  - Instead, it pauses execution at the first yield statement.
  - When you iterate over the generator (e.g., using a for loop), it resumes execution from where it left off.
  - The next value is computed and yielded.
  - The function pauses again at the next yield.
  - This process continues until there are no more yield statements or until you explicitly stop iterating.
- Benefits of Using yield:
  - Efficiency: Since it doesn't precompute all values, it's suitable for large data or infinite sequences.
  - State Preservation: The function retains its internal state between iterations. For example, it remembers where it left off.
  - Lazy Evaluation: You only compute what you need when you need it, which can be more efficient than eagerly computing everything.
- Example:

```
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for num in countdown(5):
    print(num)
```

Output:

> 5
> 4
> 3
> 2
> 1

In summary, yield allows you to create lazy generators, preserving memory and enabling efficient processing of data. 🐍✨

##### User

what does it mean "you only compute what you need when you need it" in the last sentence? I don't understand it completely

##### Copilot

Certainly! Let me explain that concept further:
When we say "you only compute what you need when you need it," we're referring to the behavior of lazy evaluation, which is a key feature of using generators with the yield keyword.
Here's what it means in more detail:

- Eager Evaluation:
  - In many programming scenarios, when you perform a computation (like a mathematical operation or a function call), it happens immediately.
  - For example, if you create a list of squared numbers [1, 4, 9, 16, 25], you compute all those values upfront and store them in memory.
  - Eager evaluation computes everything eagerly, even if you might not use all the results right away.
- Lazy Evaluation with Generators:
  - Generators, on the other hand, use lazy evaluation.
  - When you create a generator (using a function with yield), it doesn't compute all the values at once.
  - Instead, it computes each value only when you ask for it (when you iterate over the generator).
  - It generates values on-the-fly as you need them.
  - This approach is more efficient because it doesn't precompute everything and store it in memory.
- Example:
  - Let's consider the countdown example from earlier:

```
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for num in countdown(5):
    print(num)
```

- When you run this code, it doesn't compute all the countdown numbers from 5 to 1 upfront.
- Instead, it computes each number as you iterate over the generator.
- When you ask for the next value (e.g., in the for loop), it computes it at that moment.
- This way, it doesn't waste memory storing all the numbers; it only computes and provides them when needed.
In summary, lazy evaluation (as used by generators) allows you to defer computation until it's necessary, which can be more memory-efficient and responsive to your actual needs. 😊🐍
