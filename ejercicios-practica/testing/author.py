from typing import List

def calculate_median_author(numbers: List[float]) -> float:
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return round((sorted_numbers[mid1] + sorted_numbers[mid2]) / 2, 2)

numbers = [3, 6, 5, 7, 9]
median = calculate_median_author(numbers)
text = "Author code "
if median is None:
    print(f'{text} Median: None')
else:
    print(f"{text} Median: {median:.2f}")