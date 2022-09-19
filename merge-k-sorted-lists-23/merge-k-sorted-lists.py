# insert values into priority queue
# while priority queue has values: add head to result, this is necessary the next largest element
# and add the next value in the list to the queue

# Definition for singly-linked list.
from queue import PriorityQueue
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Wrapper():
    def __init__(self, node) -> None:
        self.node = node
    def __lt__ (self, other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        head = iter = ListNode(0)
        for l in lists:
            if l: 
                pq.put(Wrapper(l))
        while not pq.empty(): 
            node = pq.get().node
            iter.next = ListNode(node.val)
            iter = iter.next

            node = node.next
            if node:
                pq.put(Wrapper(node))
        return head.next

a = Solution()
print(a.mergeKLists([ListNode(0), ListNode(1), ListNode(2)]))