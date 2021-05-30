#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/30 2:11 下午
"""


from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        ans, cnt = nums[0], 1
        for val in nums[1:]:
            if val == ans:
                cnt += 1
            elif val != ans:
                if cnt == 0:
                    ans, cnt = val, 1
                else:
                    cnt -= 1
            print(ans, cnt)
        return ans
