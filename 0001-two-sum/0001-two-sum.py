class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        n = len(nums)

        #해시 테이블 만들기 
        for i in range(n):
            table[nums[i]] = i

        for i in range(n):
            pair = target - nums[i]
            if pair in table and i != table[pair]:
                return [i, table[pair]]
        




        
        

        



        