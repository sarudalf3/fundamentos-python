print('Hello World')

# 1. TAREA: imprimir "Hola mundo"
print("Hola mundo")
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Ruben"
print("Hola", name)	# con una coma
print("Hola " + name)	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
num = 21
print("Hola", num)	# con una coma
print("Hola"+ num)	# con un + - !Este debería darnos un error!
num = 21
print("Hola "+str(num))	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} and {}.".format(fave_food1, fave_food2))  # con .format()
print(f"Me encanta comer {fave_food1} and {fave_food2}.") # con una cadena f
# 5. Other methods
name = "Rube"
age = 37
print("Mi name is %s And I have %d" % (name, age))

