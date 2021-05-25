#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/25 10:20 上午
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        注意这种写法实际耗时较长，可以把pre_half最右边的点和cur比较，能减少耗时，不过时间复杂度都是一致的O(n^2)
        :param head:
        :return:
        """
        pre = ListNode(0, None)
        cur = head
        while cur:
            pre_half = pre
            while True:
                if not pre_half.next:
                    pre_half.next, cur, pre_half.next.next = cur, cur.next, None
                    break
                elif cur.val < pre_half.next.val:
                    pre_half.next, cur.next, cur= cur, pre_half.next, cur.next
                    break
                else:
                    pre_half = pre_half.next
        return pre.next
