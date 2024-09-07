from typing import List
import numpy as np

def calculate_median_student(numbers: List[float]) -> float:
    # Your code here
    if len(numbers) ==0:
        return None
    return round(np.median(numbers), 2)

numbers = [3, 6, 5, 7, 9, 1]
# Calculate median and print result
median = calculate_median_student(numbers)
text = "Students code "
if median is None:
    print(f'{text} Median: None')
else:
    print(f"{text} Median: {median:.2f}")
        
      