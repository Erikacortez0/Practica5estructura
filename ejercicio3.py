def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERRROR AL DIVIDIR ENTRE 0!!!!!")
        
print(f"Dividir = {dividir(4,2)}")
print(f"Dividir = {dividir(4,0)}")