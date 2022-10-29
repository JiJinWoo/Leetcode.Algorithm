class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            #print(nums2[nums2.index(i):])
            if max(nums2[nums2.index(i):]) > i:
                for j in nums2[nums2.index(i):]:
                    if j > i:
                        result.append(j)
                        break
            else:
                result.append(-1)

        return result