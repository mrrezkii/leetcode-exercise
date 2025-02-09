# Two Sum Problem - HashMap Approach

## Problem Statement
Given an array `nums` of integers and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You **may not use** the same element twice, and you can assume that there is always exactly **one solution**.

## Example

### **Input:**
```python
nums = [2, 7, 11, 15]
target = 9
```

### **Output:**
```python
[0, 1]
```

### **Explanation:**
`nums[0] + nums[1] = 2 + 7 = 9`, so we return `[0,1]`.

---

## Solution Using HashMap (Dictionary in Python)

### **Approach:**
1. Create an empty **dictionary (HashMap)** to store the numbers and their indices.
2. Iterate through the `nums` array:
   - Calculate the **complement**: `complement = target - nums[i]`
   - If `complement` is already in the dictionary, return the stored index and the current index.
   - Otherwise, store `nums[i]` and its index in the dictionary.
3. Return the result as `[index1, index2]`.

---

## Code Implementation

```python
def two_sum(nums, target):
    num_map = {}  # Dictionary to store (number, index)

    for i, num in enumerate(nums):
        complement = target - num  # Compute required pair

        # Check if complement is already in the dictionary
        if complement in num_map:
            return [num_map[complement], i]  # Return found indices

        # Store the number with its index
        num_map[num] = i

    return []  # Return empty list if no solution exists

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)
```

---

## Dry Run Example

### **Given Input:**
```plaintext
nums = [2, 7, 11, 15], target = 9
```

### **Execution Steps:**

| Step | `i` | `nums[i]` | `complement = target - nums[i]` | Dictionary (`num → index`) | Action |
|------|----|----------|---------------------------|------------------|---------|
| 1    | 0  | 2        | 9 - 2 = **7**             | `{2 → 0}`        | Store `2` at index `0` |
| 2    | 1  | 7        | 9 - 7 = **2**             | `{2 → 0}`        | **Found!** `2` exists at index `0` |
| 3    | -  | -        | -                         | -                | Return `[0,1]` |

✅ **Final Output:**
```plaintext
Indices: [0, 1]
```

---

## Complexity Analysis
- **Time Complexity:** `O(n)`  
  - We iterate through `nums` **once** (`O(n)`) and perform **O(1)** operations for lookups and insertions in the dictionary.
  
- **Space Complexity:** `O(n)`  
  - In the worst case, we store every element in the dictionary (`O(n)` space).

---

## Why Use a HashMap?
✅ **Fast lookups:** Checking for the complement in `O(1)` time.  
✅ **Single pass:** No need for nested loops (`O(n²)` complexity avoided).  
✅ **Preserves original indices:** No sorting needed.

---

## Alternative Approaches
### 1️⃣ **Brute Force Approach (O(n²))**
- Use two nested loops to check each pair.
- Not efficient for large inputs.

### 2️⃣ **Sorting + Two Pointers (O(n log n))**
- Sort the array first, then use two pointers to find the sum.
- Not suitable if index positions need to be preserved.

---

## Summary
- **Best Approach:** HashMap (`O(n) time, O(n) space`)
- **Brute Force:** Slow (`O(n²) time`)
- **Sorting + Two Pointers:** Only works if index order isn’t required (`O(n log n) time`)

🚀 **Use HashMap for the most efficient solution!**

