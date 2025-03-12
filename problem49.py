import collections


def groupAnagrams(strs):
    map = collections.defaultdict(list)
    for str in strs:
        key = "".join(sorted(str))
        map[key].append(str)
    return list(map.values())

if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """