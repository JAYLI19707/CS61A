# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self,head,n):
        num=head
        i=0
        while num:
            i+=1
            num=num.next
        p=head
        dummy=ListNode()
        tail=dummy
        for j in range(i-n):
            tail.next=p
            p=p.next
            tail=tail.next
        temp=p.next
        tail.next=temp
        return dummy.next

# 创建链表节点而不是列表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n=2
# 创建Solution实例
solution = Solution()
result = solution.removeNthFromEnd(head, n)

# 打印结果看看发生了什么
current = result
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next