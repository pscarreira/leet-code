from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value_list_1 = 0
        value_list_2 = 0  

        cont = 0

        while l1:
            value_list_1 = value_list_1  + l1.val * (10 ** cont)
            l1 = l1.next
            cont += 1
        
        cont = 0
        while l2:
            value_list_2 = value_list_2  + l2.val * (10 ** cont)
            l2 = l2.next
            cont += 1

        sum_values = str(value_list_1 + value_list_2)
        answer_list = None

        for digit in sum_values:
            new_digit = ListNode(digit, answer_list)
            answer_list = new_digit
            print(answer_list.val)

        return answer_list