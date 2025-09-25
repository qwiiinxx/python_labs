def transpose(nums):
    result = []
    for i in nums:
        if nums.count(i) == 0:
            return result == []
    
    n_len = len(nums[0])
    for n in nums:
        if len(n) != n_len:
            raise ValueError('рваная матрица')
        