#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 8:14 下午
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self):
        self.visited = dict()

    def cloneGraph(self, node: Node) -> Node:
        """
        递归求解的方法，也可以考虑采用非递归的方法，思路为深度搜索或者广度搜索；
        :param node:
        :return:
        """
        if not node:
            return None
        ans = Node(node.val, [])
        self.visited[node.val] = ans
        for n in node.neighbors:
            if n.val in self.visited:
                ans.neighbors.append(self.visited[n.val])
            else:
                ans.neighbors.append(self.cloneGraph(n))
        return ans
