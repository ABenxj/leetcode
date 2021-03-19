"""
给你一个字符串 s，找到 s 中最长的回文子串。

"""


class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """
        中心扩展算法，注意奇偶情况
        :param s:
        :return:
        """
        out = ''
        for i, val in enumerate(s):
            k = 0
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                k += 1
            if 2 * k - 1 > len(out):
                out = s[i - k + 1:i + k]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                k = 0
                while i - k >= 0 and i + 1 + k < len(s) and s[i - k] == s[i + 1 + k]:
                    k += 1
                k += -1
                if 2 * k + 2 > len(out):
                    out = s[i - k:i + k + 2]
        return out

    def longestPalindrome2(self, s: str) -> str:
        """
        Manacher 算法
        :param s:
        :return:
        """
        if not s:
            return ''
        # 用"#"填充字符串
        s_new = '#' + '#'.join([x for x in s]) + '#'
        # 记录臂长
        s_r = [0] * len(s_new)
        k, center = 0, 0
        max_len = 0
        for i in range(len(s_new)):
            # 可以跳过的最小的区间长度
            r = min(s_r[2 * k - i], s_r[k] + k - i)
            while i - r >= 0 and i + r < len(s_new) and s_new[i - r] == s_new[i + r]:
                r = r + 1
            s_r[i] = r - 1
            # 回文串右边界更新
            if s_r[i] + i > s_r[k] + k:
                k = i
            # 更新最长回文字符串的中心点和长度
            if s_r[i] > max_len:
                max_len = s_r[i]
                center = i
        return ''.join(s_new[center - max_len:center + max_len + 1].split('#'))
