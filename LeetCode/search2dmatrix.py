from typing import List


def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
    # step 1 is to find the row ??
    row = 0

    for i in range(len(matrix)):
        if t < matrix[i][0]:
            break
        elif t == matrix[i][0]:
            return True
        else:
            row = i


    # top, bottom = 0, len(matrix) - 1
    # while top <= bottom:
    #     mid = top + (bottom - top) // 2
    #     if t < matrix[mid][0]:
    #         bottom = mid - 1
    #     elif t > matrix[mid][-1]:
    #         top = mid + 1
    #     else:
    #         # Target is within the range of this row
    #         selected_row = matrix[mid]
    #         break
    # else:
    #     # If no valid row is found
    #     return False

    # step 2 find the item :
    arr = matrix[row]
    l = 0
    r = len(arr) - 1

    while l <= r:
        m_i = l + (r - l) // 2
        if t > arr[m_i]:
            l = m_i + 1

        elif t < arr[m_i]:
            r = m_i - 1
        else:
            return True

    return False