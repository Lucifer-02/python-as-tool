def mean_tuple(nums: tuple):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


print(mean_tuple((1, 2, 5)))
