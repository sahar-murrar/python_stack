students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, students):
    for student in students:
        for key,value in student.items():
            if(key == key_name):
                print(f"{student[key_name]}")
            
iterateDictionary2('last_name',students)            