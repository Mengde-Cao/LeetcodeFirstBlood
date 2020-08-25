"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""

"""
                               root
                 /              |                 \
level0          a               b                  c
            /   |   \       /   |    \         /   |    \ 
level1    ad    ae   af   bd    be    bf     cd    ce    cf
"""


def letterCombinations(digits: 'str') -> 'list[str]':
    res = []
    # 边界情况
    if not digits:
        return res
    num_map = {
        '0': '',
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tvu',
        '9': 'wxyz'
    }

    def dfs(digits: 'str', index: 'int', num_map: 'dict', r: 'str', res: 'list[str]'):
        """

        :param digits: 输入的数字组合，如例子中的23
        :param index: dfs遍历的层数，即输入的第几个字符
        :param num_map: 数字映射
        :param r: 当前的字母组合
        :param res: 组合结果集
        """
        # 已经走到最底层
        if len(r) == len(digits):  # or index == len(digits):
            res.append(r)
            return
        # 当前数字和对应的字母
        c = digits[index]
        letters = num_map[c]
        for l in letters:
            # 往下走
            r += l
            dfs(digits, index + 1, num_map, r, res)
            # 回到上一层
            r = r[:-1]

    dfs(digits, 0, num_map, '', res)
    return res
