def twoSum(nums, target):
    seen = {}  # 用于存储已遍历的数字及其索引
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# 示例调用
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print("结果:", result)  # 输出: [0, 1]