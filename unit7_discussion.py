import time

"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a shallow copy of the original list to avoid mutating it
    sorted_list = list(lst)
    n = len(sorted_list)

    # Outer loop to traverse through all list elements
    for i in range(n):
        # Track if any swap happens in this pass
        swapped = False

        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if sorted_list[j] > sorted_list[j+1]:
                # Swap elements if they are out of order
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True

        # If no two elements were swapped by the inner loop, then list is sorted
        if not swapped:
            break
    return sorted_list



def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list into smaller halves
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # Merge the sorted halves together
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    """Helper function to merge two sorted listed into a single sorted list."""
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements left over from either list
    result.extend(left[i:])
    result.extend(right[j:])

    return result



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # 1. Create an unsorted list containing at least 7 values
    dataset_1 = [42, 17, 99, 8, 55, 31, 23, 64]

    # 2. Display the original list
    print(f"Original List: {dataset_1}")

    # 3. Sort the list using Bubble Sort
    bubble_sorted = bubble_sort(dataset_1)

    # 4. Sort the same list using Merge Sort
    merge_sorted = merge_sort(dataset_1)

    # 5. Clearly label and display all results
    print(f"Bubble Sorted: {bubble_sorted}")
    print(f"Merge Sorted: {merge_sorted}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    # 1. Create a second dataset (at least 7 values)
    # 2. Use different values than Dataset #1 (Using a larger, reversed, or performance-test style dataset)
    dataset_2 = [105, 4, 82, 16, 50, 73, 91, 12, 38]
    print(f"Original List: {dataset_2}")

    # 3. Sort using both algorithms
    # We will also track ececution time to give a deeper performance comparison

    start_time = time.perf_counter()
    bubble_sorted_2 = bubble_sort(dataset_2)
    bubble_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    merge_sorted_2 = merge_sort(dataset_2)
    merge_time = time.perf_counter() - start_time

    print(f"Bubble Sorted: {bubble_sorted_2}")
    print(f"Merge Sorted: {merge_sorted_2}")

    # 4. Compare the results
    print("\n--- Algorithm Performance Comparison ---")
    print(f"Bubble Sort Time: {bubble_time:.8f} seconds")
    print(f"Merge Sort Time: {merge_time:.8f} seconds")
    print("\nConclusion: Both algorithms correctly ordered the elements.")
    print("Merge Sort runs in O(n log n) time, making it significantly more efficient.")
    print("than Bubble Sort's O(n^2) time complexity for large datasets.")



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # ---Edge Case 1: Empty List ---
    empty_list = []
    print(f"\nEdge Case 1: Empty list: {empty_list}")
    print(f" Bubble Sort Result: {bubble_sort(empty_list)}")
    print(f"Merge Sort Result: {merge_sort(empty_list)}")
    print(" Explanation: Both algorithms handle an empty list without crashing.")
    print(" - Bubble Sort's loops naturally do not execute since the length is 0.")
    print(" Merge Sort hits its base case (len(arr) <= 1) immediately and returns the empty list.")

    # --- Edge Case 2: List with Duplicate Values ---
    duplicates_list = [4, 2, 7, 4, 1, 2, 4]
    print(f"\nEdge Case 2: Duplicate list: {duplicates_list}")
    print(f" Bubble Sort Result: {bubble_sort(duplicates_list)}")
    print(f"Merge Sort Result: {merge_sort(duplicates_list)}")
    print(" Explanation: Both algorithms correctly sort lists containing duplicate elements.")
    print(" - Bubble sort only swaps when elements are strictly greater, keeping duplicates stable.")
    print(" - Merge Sort's comparison operator (< or <=) preserves stability or correctly groups identical elements.")


if __name__ == "__main__":
    main()