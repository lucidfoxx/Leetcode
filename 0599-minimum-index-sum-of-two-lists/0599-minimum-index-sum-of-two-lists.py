class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        minsum = 99999999
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if minsum > i+j:
                        ans = [list1[i]]
                        minsum = i+j
                    elif i+j == minsum:
                        ans.append(list1[i])
        return ans
 