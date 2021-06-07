##1- Update values in lists and dictionaries

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

#En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

#Camba el valor 20 en z a 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

##2- Loop by dictionary lists 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for val in students:
    print('first_name - '+val['first_name']+', last_name - '+val['last_name'])

# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel