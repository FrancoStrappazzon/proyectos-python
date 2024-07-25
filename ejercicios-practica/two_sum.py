#Dado un arreglo de numeros enteros y un numero target, retorna el indice de 2 numeros los cuales sumados dan el target.
#Puedes asumir que hay exactamente una sola solucion y no se puede usar el mismo elemento 2 veces
#Podes retornar la respuesta en cualquier orden
#example: Input: nums = [2,7,11,15], target = 9. Output: [0,1]

def two_sum(nums, target):
    for i in range(len(nums)):
        
        for j in range(i+1, len(nums)):
            resultado = nums[i] + nums[j]
            
            if resultado == target:
                output = [i,j]
                
    return output
    
print(two_sum([1,11,2,7,51,35],8))