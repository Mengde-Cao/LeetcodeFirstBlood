"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generateParenthesis(n: int) -> list[str]:
    result = []
    if not n:
        return result

    def bracket(res='', left_num=0, right_num=0):
        if left_num == n and right_num == n:
            result.append(res)
            return
        if left_num < n:
            bracket(res + '(', left_num + 1, right_num)
        if right_num < left_num:
            bracket(res + ')', left_num, right_num + 1)

    bracket()
    return result
