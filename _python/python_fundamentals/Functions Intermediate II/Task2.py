students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# first solution    
def iterateDictionary(students):
    for student in students: #student here perform the value in the dictionary, but if we used range it will perform the index
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students)

#second solution:
def iterateDictionary(students):
    for student in students:
        for key,value in student.items(): #ket and value can be any name we want, they are not something static.
            print(f"{key} - {value}", end=", ") #end=", " to print the first and last name beside each other
        print("")#to print a new line    

iterateDictionary(students)
