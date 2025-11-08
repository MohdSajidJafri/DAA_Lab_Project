"""
Sorting Algorithms Implementation
Demonstrates various sorting algorithms with time complexity analysis
"""

import time
from typing import List, Callable


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²) - Worst case, Average case
    Space Complexity: O(1) - In-place sorting
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n) - Worst case, Average case, Best case
    Space Complexity: O(n) - Additional space for merging
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n) - Average case, O(n²) - Worst case
    Space Complexity: O(log n) - Recursion stack
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def measure_time(func: Callable, arr: List[int]) -> tuple:
    """Measure execution time of a sorting function"""
    start_time = time.time()
    sorted_arr = func(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return sorted_arr, execution_time


def compare_sorting_algorithms(arr: List[int]) -> None:
    """Compare different sorting algorithms"""
    print(f"\nSorting array of size {len(arr)}")
    print("=" * 60)
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    results = {}
    
    for name, func in algorithms.items():
        sorted_arr, exec_time = measure_time(func, arr)
        results[name] = {
            "time": exec_time,
            "sorted": sorted_arr
        }
        print(f"{name:15} | Time: {exec_time:.4f} ms")
    
    print("=" * 60)
    
    # Verify all algorithms produce the same result
    sorted_arrays = [result["sorted"] for result in results.values()]
    if all(arr == sorted_arrays[0] for arr in sorted_arrays):
        print("✓ All algorithms produced the same sorted result")
    else:
        print("✗ Algorithms produced different results")

