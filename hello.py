#print("hello world")

#name = input("best country in the world: ")
#print(name)

'''
name = name.lower()
if (name == "canada"):
    print("--------")
    print(name + " is the best!")
elif (name == "norway"):
    print(name + " is the 2nd best!")
else:
    print("booo wrong answer")
'''

fruits = ['applepen,grannysmith,gala','orange,mandarin,bloodorange','banana,big,small','peach,sweet,not sweet']
for fruit in fruits:
    templist = fruit.split(",")
    print(fruit)
    print(templist)

