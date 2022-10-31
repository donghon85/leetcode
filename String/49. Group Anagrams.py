class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs:
            temp = ''.join(sorted(str))
            dict[temp].append(str)
        return dict.values()