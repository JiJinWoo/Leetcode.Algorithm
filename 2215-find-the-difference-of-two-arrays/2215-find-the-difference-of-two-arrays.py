class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        
        res = []
        
        dct1 = defaultdict(int)
        dct2 = defaultdict(int)
        
        for num in num1:
            dct1[num] += 1
            
        for num in num2:
            dct2[num] += 1
        
        for item in dct1.items():
            if item[0] in nums2:
                num2.remove(item[0])
        
        for item in dct2.items():
            if item[0] in nums1:
                num1.remove(item[0])
                
        res.append(num1)
        res.append(num2)
        
        return res