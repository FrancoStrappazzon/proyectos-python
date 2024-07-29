#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most
# twice. The relative order of the elements should be kept the same.
#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of
# the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the
# final result. It does not matter what you leave beyond the first k elements.

from collections import defaultdict


def removeDuplicates(nums):
        lista_nueva = []
        count = defaultdict(int)
        for numero in nums:
            if count[numero] <2 :
                lista_nueva.append(numero)
                count[numero] +=1
            

        nums[:] = lista_nueva
        k = len(nums)
        return k
    
nums = [1,2,2,2,3,4,5,5,6,6,6]
print(removeDuplicates(nums))