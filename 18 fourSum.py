#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date:
"""


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        遍历前两个数， 后面两个采用双指针， 注重规则减少时间复杂度
        :param nums:
        :param target:
        :return:
        """
        ans = []
        nums.sort()
        len_nums = len(nums)
        # 枚举前两个数
        for i in range(len_nums-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                continue
            for j in range(i + 1, len_nums-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + 3*nums[j] > target:
                    break
                if nums[i] + nums[j] + 2*nums[-1] < target:
                    continue
                left, right = j+1, len_nums-1
                while left < right:
                    f_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if f_sum < target:
                        left += 1
                    elif f_sum > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1

        return ans
