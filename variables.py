x = 1 #int
y = 2.5 #float
name = 'mason' #strings
isStrong = True #boolean

#Multiple Line Comment
x,y,name,isStrong = (24, 45.6, 'Max', False)
print(f'all variables Output: {type(x)}, {type(y)}, {type(name)}, {type(isStrong)}')

#Casting
x = str(x)
y = int(y)
z = float(y)
isStrong = str(isStrong)
print(type(z), z)