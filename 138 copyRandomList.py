#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/22 7:53 上午
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.visited = dict()

    def copyRandomList(self, head: Node) -> Node:
        """
        类似于图的深拷贝， 考虑dfs或者bfs
        :param head:
        :return:
        """
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        new_node = Node(head.val, None, None)
        self.visited[head] = new_node
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        return new_node
