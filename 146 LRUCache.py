#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/25 8:16 上午
"""


class LinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next, self.tail.pre = self.tail, self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.move_to_end(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_end(self.cache[key])
        else:
            if self.size == self.capacity:
                self.cache.pop(self.head.next.key)
                self.remove_head()
                self.size += -1
            self.cache[key] = LinkNode(key, value)
            self.add_end(self.cache[key])
            self.size += 1

    def add_end(self, key):
        self.tail.pre.next = key
        key.next = self.tail
        key.pre = self.tail.pre
        self.tail.pre = key

    def move_to_end(self, key):
        key.pre.next = key.next
        key.next.pre = key.pre
        self.add_end(key)

    def remove_head(self):
        rm_node = self.head.next
        self.head.next = self.head.next.next
        rm_node.next.pre = self.head
        rm_node.next, rm_node.pre = None, None
