from typing import List


def evalRPN(self, tokens: List[str]) -> int:
    op_stk = []
    for t in tokens:
        if t not in "+-*/":
            op_stk.append(int(t))
        else:
            val1 = op_stk.pop()
            val2 = op_stk.pop()
            res = 0

            if t == "+":
                res = val1 + val2
            elif t == "-":
                res = val2 - val1
            elif t == "*":
                res = val1 * val2
            else:
                res = int(val2 / val1)

            op_stk.append(res)

    return op_stk[0]