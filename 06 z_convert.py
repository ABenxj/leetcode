"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Z 字形变换, 通过一个标识符，确定字符所在行；

        :param s:
        :param numRows:
        :return:
        """
        if numRows == 1:
            return s
        string_list = ['']*numRows
        weight = 1
        cur_index = 0
        for val in s:
            string_list[cur_index] += val
            cur_index += weight
            if cur_index == numRows-1 or cur_index == 0:
                weight = -1*weight
        return ''.join(string_list)
