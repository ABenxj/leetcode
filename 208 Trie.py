#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/8 8:16 上午
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.lookup
        for w in word:
            if w not in temp:
                temp[w] = {}
            temp = temp[w]
        temp['0'] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.lookup
        for w in word:
            if w not in temp:
                return False
            temp = temp[w]
        if '0' not in temp: return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.lookup
        for w in prefix:
            if w not in temp:
                return False
            temp = temp[w]
        return True
