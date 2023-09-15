def sumar(a,*args):
    for numero in args:
        a+=numero
    return a
print(f"La suma es {sumar(1,2)}")
print(f"La suma es {sumar(1,2,4,4)}")
print(f"La suma es {sumar(1,2,3,5,4,6)}")