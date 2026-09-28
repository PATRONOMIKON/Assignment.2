"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0
    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    results = find_strings_with(strings[1:], target)
    if target in strings[0]:
        return [strings[0]] + results
    return results


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """
    if os.path.isfile(directory_path):
        return 1

    total = 0
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            total += 1
        elif os.path.isdir(item_path):
            total += count_files(item_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    infected_files = []

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            if item_path.endswith(extension):
                infected_files.append(item_path)
        elif os.path.isdir(item_path):
            infected_files.extend(find_infected_files(item_path, extension))

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - COMPLETED SOLUTION")

    # Warm-up tests
    print("\nWarm-up tests:")
    print("sum_list([1, 2, 3, 4]) =", sum_list([1, 2, 3, 4]))
    print("sum_list([]) =", sum_list([]))
    print("sum_list([5, 5, 5]) =", sum_list([5, 5, 5]))

    print("count_even([1, 2, 3, 4, 5, 6]) =", count_even([1, 2, 3, 4, 5, 6]))
    print("count_even([1, 3, 5]) =", count_even([1, 3, 5]))
    print("count_even([2, 4, 6]) =", count_even([2, 4, 6]))

    print("find_strings_with(['hello', 'world', 'help', 'test'], 'hel') =",
          find_strings_with(["hello", "world", "help", "test"], "hel"))
    print("find_strings_with(['cat', 'dog', 'bird'], 'z') =",
          find_strings_with(["cat", "dog", "bird"], "z"))

    # Count files tests
    print("\nCount files tests:")
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat"))
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested"))
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected"))
    print("Total files (breach_data):", count_files("breach_data"))

    # Infected file tests
    print("\nFind infected files tests:")
    print("Total Infected Files (Test Case 1):",
          len(find_infected_files("test_cases/case1_flat")))
    print("Total Infected Files (Test Case 2):",
          len(find_infected_files("test_cases/case2_nested")))
    print("Total Infected Files (Test Case 3):",
          len(find_infected_files("test_cases/case3_infected")))

    infected = find_infected_files("breach_data")
    print("Total Infected Files (breach_data):", len(infected))

    # Department analysis requested by the assignment.
    print("\nDepartment infection counts:")
    for department in ["Finance", "HR", "Sales"]:
        department_path = os.path.join("breach_data", department)
        if os.path.isdir(department_path):
            department_infected = find_infected_files(department_path)
            print(f"{department}: {len(department_infected)}")
        else:
            print(f"{department}: department folder not generated")
