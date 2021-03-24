"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。


示例1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        基本思路：通过dict保存字符及其最新位置，更新最大的长度；
        注意点：边界问题，长度计算和更新问题
        :param s:
        :return:
        """
        if not s:
            return 0
        str_dict = dict()
        max_len, s_index = 0, 0
        for i, val in enumerate(s):
            if val in str_dict:
                if str_dict[val] >= s_index:
                    max_len = max(max_len, i - s_index)
                    s_index = str_dict[val] + 1
            str_dict[val] = i
        max_len = max(max_len, i - s_index+1)
        return max_len
