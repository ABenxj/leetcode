
"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        # 双指针从前后遍历
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                return sorted([index[left], index[right]])
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    nums = [3, 4, 2]
    target = 6
    res = [1, 2]
    st = Solution()
    assert st.twoSum(nums, target) == res
