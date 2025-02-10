class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class _Solution(object): # 18ms
    def addTwoNumbers(self, l1, l2):

        newL1 = self.extractNumbers(self.reverseLinkedList(l1))
        newL2 = self.extractNumbers(self.reverseLinkedList(l2))

        total = newL1 + newL2
        totalReverseString = str(total)[::-1]
        totalIntList = list(map(int, totalReverseString))

        result = self.buildLinkedList(totalIntList)
        return result

    def reverseLinkedList(self, node):
        prev = None
        current = node

        while current is not None:
            # Store next
            nextNode = current.next

            # Reverse current node's next pointer
            current.next = prev

            # Move pointers one position ahead
            prev = current
            current = nextNode

        return prev

    def extractNumbers(self, node):
        current = node

        result = []

        while current is not None:
            result.append(current.val)
            current = current.next

        return int(''.join(map(str, result)))

    def buildLinkedList(self, nums):
        head = ListNode(val=nums[0])
        current = head

        for i in range(1, len(nums)):
            current.next = ListNode(val=nums[i])
            current = current.next

        return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            newNode = ListNode(total % 10)

            current.next = newNode
            current = newNode

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


solution = Solution()
l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
result = solution.addTwoNumbers(l1, l2)
print(result)
print(type(result))
#
# debug = solution.buildLinkedList([1,2,3,4])
# print(debug)