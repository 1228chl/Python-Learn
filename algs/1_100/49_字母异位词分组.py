"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

提示：
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # defaultdict(type)会默认在遇到没有的键值创建一个type类型的值
        h = defaultdict(list)
        # 挨个遍历传递过来的字符串
        for s in strs:
            # 使用join()+sorted()方法达到排序后合并的效果，可以将异位词变统一
            sc = "".join(sorted(s))
            # 词典里键值唯一，sc是排序好后的统一值，可以达到去重的效果
            # 这里的.append()方法可以在键值一致的情况下，在后面追加值
            h[sc].append(s)
        # 最后返回一个list类型的值
        return list(h.values())

str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(str_list))