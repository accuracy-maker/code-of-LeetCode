"""
给你两个"非空"的链表，表示两个非负的整数。
它们每位数字都是按照"逆序"的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val    # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            l1.val %= 10
        
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1

sl = Solution()
def init_singlelist():
    l1 = ListNode()
    l1.next = None
    ptr = l1
    select = 0

    while select != 2:
        print("(1)add (2)quit=>")
        try:
            select = int(input('input an option:'))
        except ValueError:
            print("ValueError")
            print("input again\n")

        if select==1:
            new_data=ListNode()
            new_data.value = input("value:")
            ptr.next = new_data
            new_data.next = None
            ptr = ptr.next
        
    return l1

l1 = init_singlelist()
l2 = init_singlelist()

l3 = sl.addTwoNumbers(l1,l2)

def traverse_list(l3):
    ptr = l3.next
    while ptr!=None:
        print(ptr.value)
        ptr = ptr.next

traverse_list(l3)

        