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

# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

for val in students:
    name = list(val.keys())
    value = list(val.values())    
    print(name[0]+' - '+value[0]+', '+name[1]+' - '+value[1])

def iterateDictionary2(key, dict):
    for val in dict:
        print(val[key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4- Dict loop using list names
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for k, v in dojo.items():
    print(len(v),k)
    for sub in v:
        print(sub)
    print('')