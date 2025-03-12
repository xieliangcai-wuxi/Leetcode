def two_num(nums:list[int],target:int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

if __name__ == '__main__':
    print(two_num([1,2,3,4,5],9))