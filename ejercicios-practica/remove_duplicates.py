#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
#The remaining elements of nums are not important as well as the size of nums.Return k.

def removeDuplicates(nums):
    lista_sin_duplicados =[]
    for numero in nums:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)
            
    nums[:] = lista_sin_duplicados #Actualizo la lista original
    k = len(nums)
    return k
    
nums = [1,2,5,5,6,8,15,22,34,34,34,65,128,133,133]

print(removeDuplicates(nums))