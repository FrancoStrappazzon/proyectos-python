#Dados 2 arreglos ordenados nums1 and nums2 de tamaño m y n respectivamente, returnar la mediana de los 2 arreglos.

def median_arrays(array1, array2):
    #uno ambos arreglos
    merge_array = sorted((array1 + array2))
    
    n = len(merge_array)
    
    #si es par hago el promedio de los elementos centrales
    if n%2 == 0:
        median = (merge_array[n//2-1] + merge_array[n//2]) /2
    #si es impar tomo el elemento del centro
    else:
        median = merge_array[n//2]
        
    return median

print(median_arrays([1,2,6],[5,9]))