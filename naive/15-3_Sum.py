"""
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# 执行用时: 11728 ms, 在3Sum的Python3提交中击败了0.99% 的用户
# 内存消耗: 603.8 MB, 在3Sum的Python3提交中击败了0.92% 的用户
def threeSum1(nums: 'List[int]') -> 'List[List[int]]':
    nums.sort()
    r = []
    s = dict()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            target = -(nums[i] + nums[j])
            if target in s and s[target] not in (i, j):
                r.append([i, j, s[target]])
            s[nums[j]] = j
        s[nums[i]] = i
    result = set()
    if r:
        for rr in r:
            tmp = [nums[rr[0]], nums[rr[1]], nums[rr[2]]]
            tmp.sort()
            tmp = [str(t) for t in tmp]
            result.add('|'.join(tmp))
    return [list(map(int, rs.split('|'))) for rs in result]


# 超时
def threeSum2(nums: 'List[int]') -> 'List[List[int]]':
    import itertools
    nums.sort()
    result = []
    for i, j, k in itertools.combinations(nums, 3):
        if i + j + k == 0 and [i, j, k] not in result:
            result.append([i, j, k])
    return result


# 双指针
def threeSum3(nums: 'List[int]') -> 'List[List[int]]':
    result = []
    if not nums or len(nums) < 3:
        return result
    nums.sort()
    index = 0
    while index < len(nums) - 2:
        if index > 0 and nums[index] == nums[index - 1]:
            index += 1
            continue
        left = index + 1
        right = len(nums) - 1
        base = nums[index]
        while left < right:
            sum = base + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([base, nums[left], nums[right]])
                right -= 1
                left += 1
                # 处理重复的情况
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        index += 1
    return result


if __name__ == '__main__':
    pass
