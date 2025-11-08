# Design and Analysis of Algorithms - Lab Project

A simple demonstration project showcasing fundamental sorting and searching algorithms with time complexity analysis.

## Project Overview

This project implements and compares various algorithms commonly studied in Design and Analysis of Algorithms courses:

- **Sorting Algorithms**: Bubble Sort, Merge Sort, Quick Sort
- **Searching Algorithms**: Linear Search, Binary Search

Each algorithm includes:
- Complete implementation
- Time complexity analysis
- Space complexity analysis
- Performance comparison

## Algorithms Implemented

### Sorting Algorithms

1. **Bubble Sort**
   - Time Complexity: O(n²)
   - Space Complexity: O(1)
   - Best for: Small arrays, educational purposes

2. **Merge Sort**
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - Best for: Large arrays, when stability is required

3. **Quick Sort**
   - Time Complexity: O(n log n) average, O(n²) worst case
   - Space Complexity: O(log n)
   - Best for: General-purpose sorting, fast in practice

### Searching Algorithms

1. **Linear Search**
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Works on: Unsorted arrays

2. **Binary Search**
   - Time Complexity: O(log n)
   - Space Complexity: O(1)
   - Works on: Sorted arrays only

## Project Structure

```
DAA_Lab/
├── main.py                  # Main demonstration file
├── sorting_algorithms.py    # Sorting algorithms implementation
├── searching_algorithms.py  # Searching algorithms implementation
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Requirements

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/MohdSajidJafri/DAA_Lab_Project.git
cd DAA_Lab_Project
```

2. Run the main program:
```bash
python main.py
```

The program will:
- Generate random arrays of different sizes
- Demonstrate sorting algorithms with execution time comparison
- Demonstrate searching algorithms with execution time comparison
- Display time complexity analysis for each algorithm

## Sample Output

The program generates output showing:
- Execution time for each algorithm
- Comparison between different algorithms
- Time complexity analysis
- Verification that algorithms produce correct results

## Learning Objectives

This project demonstrates understanding of:
- Algorithm implementation
- Time complexity analysis (Big O notation)
- Space complexity analysis
- Algorithm comparison and selection
- Performance measurement

## Author

Created as part of Design and Analysis of Algorithms Lab coursework.

## License

This project is created for educational purposes.

