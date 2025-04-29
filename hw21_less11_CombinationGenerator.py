def combination_generator(nums):
    if len(nums) <= 1:
        yield nums
    else:
        for i in range(len(nums)):
            res = nums[:i] + nums[i + 1:]
            for j in combination_generator(res):
                yield [nums[i]] + j


numbers = [1, 2, 3]
for num in combination_generator(numbers):
    print(num)
