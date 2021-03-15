"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = ListNode(0)
        out_cur, div = out, 0
        while l1 or l2 or div:
            if not l1 and not l2:
                div, mod = 0, div
            elif not l1:
                div, mod = divmod(l2.val + div, 10)
                l2 = l2.next
            elif not l2:
                div, mod = divmod(l1.val + div, 10)
                l1 = l1.next
            else:
                div, mod = divmod(l1.val + l2.val + div, 10)
                l1 = l1.next
                l2 = l2.next
            out_cur.next = ListNode(mod)
            out_cur = out_cur.next
        return out.next


def list_to_ListNode(list):
    ln = ListNode(0)
    ln_cp = ln
    for item in list:
        ln.next = ListNode(item)
        ln = ln.next
    return ln_cp.next


def ListNode_TO_list(listnode):
    ret = []
    while listnode:
        ret.append(listnode.val)
        listnode = listnode.next
    return ret


if __name__ == '__main__':
    l1 = list_to_ListNode([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_ListNode([9, 9, 9, 9])
    res = list_to_ListNode([8, 9, 9, 9, 0, 0, 0, 1])
    st = Solution()
    out = st.addTwoNumbers(l1, l2)
    print(ListNode_TO_list(out), ListNode_TO_list(res))
