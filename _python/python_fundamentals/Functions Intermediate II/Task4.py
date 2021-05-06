dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key, value in dict.items():
        print(f"{len(value)} {key.upper()}") 
        for i in value:
            print(i)
        print("")    

      

printInfo(dojo)