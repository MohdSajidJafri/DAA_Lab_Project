"""
Searching Algorithms Implementation
Demonstrates linear and binary search algorithms with complexity analysis
"""

import time
from typing import List, Optional, Callable


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """
    Linear Search Algorithm
    Time Complexity: O(n) - Worst case, Average case
    Space Complexity: O(1)
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Binary Search Algorithm (requires sorted array)
    Time Complexity: O(log n) - Worst case, Average case
    Space Complexity: O(1) - Iterative, O(log n) - Recursive
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


def measure_search_time(func: Callable, arr: List[int], target: int) -> tuple:
    """Measure execution time of a search function"""
    start_time = time.time()
    result = func(arr, target)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return result, execution_time


def compare_searching_algorithms(arr: List[int], target: int) -> None:
    """Compare linear search vs binary search"""
    print(f"\nSearching for {target} in array of size {len(arr)}")
    print("=" * 60)
    
    # Linear search (works on unsorted arrays)
    linear_result, linear_time = measure_search_time(linear_search, arr, target)
    print(f"Linear Search  | Index: {linear_result} | Time: {linear_time:.6f} ms")
    
    # Binary search (requires sorted array)
    sorted_arr = sorted(arr)
    binary_result, binary_time = measure_search_time(binary_search, sorted_arr, target)
    print(f"Binary Search  | Index: {binary_result} | Time: {binary_time:.6f} ms")
    
    print("=" * 60)
    
    if linear_result is not None:
        print(f"✓ Target {target} found at index {linear_result}")
    else:
        print(f"✗ Target {target} not found in the array")
    
    if linear_result == binary_result:
        print("✓ Both algorithms found the same result")
    
    # Performance comparison
    if linear_time > 0 and binary_time > 0:
        speedup = linear_time / binary_time
        print(f"\nBinary search is {speedup:.2f}x faster than linear search")

