from typing import List


def dailyTemperatures(self, temps: List[int]) -> List[int]:
    res = [0] * len(temps)
    temp_stk = []

    for i in range(len(temps)):

        while temp_stk and temps[i] > temps[temp_stk[len(temp_stk) - 1]]:
            res[temp_stk[len(temp_stk) - 1]] = i - temp_stk[len(temp_stk) - 1]
            temp_stk.pop()

        temp_stk.append(i)

    return res