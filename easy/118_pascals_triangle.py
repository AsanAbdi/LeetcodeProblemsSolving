from typing import List


class Solution:
    def generate(self, num: int) -> List[List[int]]:
        if num == 1:
            return [[1]]
        list = [[1], [1,1]]
        counter = 2
        while counter < num:
            list_to_add = []
            for i in range(len(list[-1])-1):
                list_to_add.append(list[-1][i] + list[-1][i+1])
            list_to_add.insert(0, 1)
            list_to_add.append(1)

            list.append(list_to_add)
            counter += 1
        return list