from typing import List


def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    res = []

    def backTrack(on, cn):
        if on == cn == n:
            res.append("".join(stack))
            return

        if on < n:
            stack.append('(')
            backTrack(on + 1, cn)
            stack.pop()

        if cn < on:
            stack.append(')')
            backTrack(on, cn + 1)
            stack.pop()

    backTrack(0, 0)
    return res