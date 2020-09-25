# https://leetcode.com/problems/utf-8-validation/
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        for i in range(len(data)):
            binary = bin(data[i])[2:].zfill(8)

            if binary[:2] == '10':
                continue

            count = binary[:4].count('1')

            if count == 0:
                continue
            elif count == 2:
                if not data[i + 1] or bin(data[i + 1]).zfill(8)[2:4] != '10':
                    return False
            elif count == 3:
                if (not data[i + 1] or not data[i + 2]) or (
                        bin(data[i + 1]).zfill(8)[2:4] != '10' or bin(data[i + 2]).zfill(8)[2:4] != '10'):
                    return False
            elif count == 4:
                if (not data[i + 1] or not data[i + 2] or not data[i + 3]) or (
                        bin(data[i + 1]).zfill(8)[2:4] != '10' or bin(data[i + 1]).zfill(8)[2:4] != '10' or bin(data[i + 3]).zfill(8)[2:4]):
                    return False

        return True

# I knew it wouldn't be the best code with too many repetitive lines
# then, IndexError: list index out of range comes out

# >> (number) - change the place value up to number to the left
# << (number) - to the right

# change the place value of the given number by >> operation to check if they start with (0b)0, (0b)110, (0b)1110, or (0b)1110
# then check the next elements, if they have 10 at the beginning: 0 - doesn't need to be checking / 110 - one 10 /
# 1110 - two 10 / 11110 - three 10


