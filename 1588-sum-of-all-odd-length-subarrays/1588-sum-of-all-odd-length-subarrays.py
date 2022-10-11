class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        
        for i in range(len(arr)):
            sum = []
            sum.append(arr[i])
            result += sum[0]
            for j in range(i+1, len(arr)):
                sum.append(arr[j])
                print(sum)
                if len(sum) % 2 == 1:
                    for k in range(len(sum)):
                        result += sum[k]
                        
        return result