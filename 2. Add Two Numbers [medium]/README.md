# Add Two Numbers - LeetCode Problem

## Problem Statement
You are given two **non-empty** linked lists representing two **non-negative integers**. The digits are stored in **reverse order**, and each of their nodes contains a **single digit**. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

### Example 1:
#### **Input:**  
```
l1 = [2,4,3]
l2 = [5,6,4]
```
#### **Output:**  
```
[7,0,8]
```
#### **Explanation:**  
```
342 + 465 = 807 (stored as [7,0,8])
```

### Example 2:
#### **Input:**  
```
l1 = [0]
l2 = [0]
```
#### **Output:**  
```
[0]
```

### Example 3:
#### **Input:**  
```
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```
#### **Output:**  
```
[8,9,9,9,0,0,0,1]
```
#### **Explanation:**  
```
9999999 + 9999 = 10009998 (stored as [8,9,9,9,0,0,0,1])
```

---

## **Solution**
### **Approach**
Instead of converting the linked lists into integers and performing addition, we directly traverse both linked lists **digit by digit** while keeping track of a `carry` value.

1. Start with a dummy node to simplify list construction.
2. Use a `carry` variable to handle sums greater than 9.
3. Traverse both linked lists simultaneously, adding corresponding digits.
4. Store the sum modulo 10 as a new node, and update `carry`.
5. Move to the next node in both lists.
6. If a carry remains after traversal, add an extra node.

### **Optimized Python Solution**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy head to simplify result list handling
        current = dummy
        carry = 0  # Carry to hold overflow values

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1, else 0
            val2 = l2.val if l2 else 0  # Get value from l2, else 0

            # Compute sum and new carry
            total = val1 + val2 + carry
            carry = total // 10  # Extract carry
            newNode = ListNode(total % 10)  # Store remainder in new node
            
            current.next = newNode  # Link new node to result list
            current = newNode  # Move pointer forward

            # Move to next nodes in l1 and l2 if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # Return actual head (dummy.next)
```

---

## **Complexity Analysis**
### **Time Complexity: O(max(N, M))**
- We traverse both linked lists **once**. Since we only iterate through the longest list, the time complexity is **O(max(N, M))**, where `N` and `M` are the lengths of `l1` and `l2`.

### **Space Complexity: O(max(N, M))**
- We create a new linked list to store the result, which has at most `max(N, M) + 1` nodes (if there is an extra carry at the end).
- Thus, space complexity is **O(max(N, M))**.

---

## **Why is This Solution Efficient?**
✅ **Avoids Integer Conversion**: No need to convert linked lists to integers and back.  
✅ **Processes in One Pass**: Only **one traversal** is required, making it time-efficient.  
✅ **Handles Carry Efficiently**: The carry is handled while iterating, avoiding extra iterations.  
✅ **No Additional Data Structures**: Uses only a few extra pointers and variables.

---

## **Alternative (Less Efficient) Approach**
Some solutions reverse both linked lists, convert them to integers, sum them up, and then create a new linked list from the sum. This is **slower** because:
1. **Reversing the list takes extra time**: O(N) for both lists.
2. **Converting to integers takes extra time**: Can be O(N) due to string operations.
3. **String manipulations add overhead**: str() and join() operations slow down execution.

Thus, the optimized solution is better for both **speed and memory usage**.

---

## **Final Thoughts**
This problem is an excellent exercise in linked list traversal and basic arithmetic operations. The optimized approach ensures that we minimize unnecessary computations while keeping the implementation **clean and readable**. 🚀

