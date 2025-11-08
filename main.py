"""
Main demonstration file for DAA Lab Project
Demonstrates sorting and searching algorithms with complexity analysis
"""

import random
from sorting_algorithms import compare_sorting_algorithms
from searching_algorithms import compare_searching_algorithms


def generate_random_array(size: int, min_val: int = 1, max_val: int = 1000) -> list:
    """Generate a random array of integers"""
    return [random.randint(min_val, max_val) for _ in range(size)]


def demonstrate_sorting_algorithms():
    """Demonstrate different sorting algorithms"""
    print("\n" + "=" * 60)
    print("SORTING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    # Test with different array sizes
    test_sizes = [100, 500, 1000]
    
    for size in test_sizes:
        arr = generate_random_array(size)
        compare_sorting_algorithms(arr)
    
    print("\n" + "=" * 60)
    print("TIME COMPLEXITY ANALYSIS:")
    print("=" * 60)
    print("Bubble Sort: O(n²) - Simple but inefficient for large arrays")
    print("Merge Sort:  O(n log n) - Consistent performance, stable")
    print("Quick Sort:  O(n log n) average, O(n²) worst - Fast in practice")
    print("=" * 60)


def demonstrate_searching_algorithms():
    """Demonstrate different searching algorithms"""
    print("\n" + "=" * 60)
    print("SEARCHING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    # Test with different array sizes
    test_sizes = [1000, 10000, 100000]
    
    for size in test_sizes:
        arr = generate_random_array(size)
        # Search for a random element from the array
        target = random.choice(arr)
        compare_searching_algorithms(arr, target)
    
    print("\n" + "=" * 60)
    print("TIME COMPLEXITY ANALYSIS:")
    print("=" * 60)
    print("Linear Search: O(n) - Works on unsorted arrays")
    print("Binary Search: O(log n) - Requires sorted array, much faster")
    print("=" * 60)


def main():
    """Main function to run all demonstrations"""
    print("\n" + "=" * 60)
    print("DESIGN AND ANALYSIS OF ALGORITHMS - LAB PROJECT")
    print("=" * 60)
    print("This project demonstrates various algorithms with complexity analysis")
    print("=" * 60)
    
    # Demonstrate sorting algorithms
    demonstrate_sorting_algorithms()
    
    # Demonstrate searching algorithms
    demonstrate_searching_algorithms()
    
    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()

