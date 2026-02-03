calc = input("Expression")
x,y,z = calc.split(" ")
newx = int(x)
newz = int(z)
if y == "+":
    result = newx+newz
elif y == "-":
    result= newx-newz
elif y== "*":
    result= newx*newz
elif y== "/" and z == 0:
    print("cant solve")
    
elif y== "/":
    result= newx/newz

print (float(result))
