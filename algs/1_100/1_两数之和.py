"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 定义字典进行存储和去重操作
        h = dict()
        # 使用enumerate进行索引和值的同时操作
        for i,j in enumerate(nums):
            # 判断target减去j的差值是否存在与字典中
            if target - j in h:
                # 存在则直接返回输出
                return [h[target - j], i]
            # 不存在则进行字典存储，方便下一次进行比对
            h[j] = i

s = Solution()
print(s.twoSum([2,5,11,4,15], 9))