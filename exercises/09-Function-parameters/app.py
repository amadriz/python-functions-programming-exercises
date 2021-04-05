# Your code goes here:
def render_person(name, birthday, color, age, male):
    
    param = name + " is a " + str(age) + " years old " + male + " born in " + birthday + " with " + color + " eyes" 
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))