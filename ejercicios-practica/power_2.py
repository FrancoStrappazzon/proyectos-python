#Hacer una funcion que reciba un array de enteros y devuelva un array de enteros con los numeros que son potencias de 2 indicando 1 (si es potencia) o 0 (si no)

def isPower(arr):
    new_array=[]
    for num in arr:
        #verifico que sea par y mayor de 1
        while ((num%2)==0) & (num>1): 
            #voy actualizando el valor de num a la mitad , si es potencia de 2 al final me queda un 1 en ese valor : 8/2= 4/2= 2/2 = 1
            num = num/2
        #si el numero resultante es 1 significa que es potencia de 2
        if num==1:
            new_array.append(1)
        else:
            new_array.append(0)
    return new_array

arr =[1,2,3,8,16,32,34,40,64,128,200,256]

print(isPower(arr))