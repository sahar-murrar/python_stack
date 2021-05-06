
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changeList(x):
    for i in range(0, len(x),1):
        for j in range(0, len(x[i]),1):
            if x[i][j] ==10:
                x[i][j]=15
    return x            

y=changeList(x)
print(y)

# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
def changelistofdict(students):
    for i in range(0, len(students),1):
        if i==0:
           students[i].update(last_name='Bryant') 
    return students       

u=changelistofdict(students)
print(u)

# 3.In the sports_directory, change 'Messi' to 'Andres'
def updatedictionary(dic):      
    s=dic.get('soccer')
    for i in range(len(s)):
        s[0]='Andres'
    return dic    

#sports_directory.update(soccer=['Andres', 'Ronaldo', 'Rooney'])
w=updatedictionary(sports_directory)
print(w)

# 4.Change the value 20 in z to 30
def changearrayofdic(arr):
     arr[0].update(y=30) 

     return arr

q=changearrayofdic(z)
print(q)     
