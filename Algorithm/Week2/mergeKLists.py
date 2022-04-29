# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        return self.merge(lists, 0, len(lists) - 1) #调用归并排序函数
    def merge(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r: return lists[l]
        return self.mergeTwoLists(self.merge(lists, l, (l + r) // 2), self.merge(lists, (l + r) // 2 + 1, r)) 
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) #构造虚节点
        move = dummy #设置移动节点等于虚节点
        while l1 and l2: #都不空时
            if l1.val < l2.val:
                move.next = l1 #移动节点指向数小的链表
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2 #连接后续非空链表
        return dummy.next #虚节点仍在开头
