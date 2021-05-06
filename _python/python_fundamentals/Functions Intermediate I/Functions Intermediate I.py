import random
def randInt(min=0, max=100):
    if min >max or max <0:
        print("error!")
    else:

        num = min+(random.random()*(max-min))
        return round(num)


x=randInt()
print(x)
y=randInt(50)
print(y)
z=randInt(max=500)
print(z)
w=randInt(50,300)
print(w)