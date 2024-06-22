def sum_nums(nums):
   

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    total = 0

    for num in nums:
        total = total + num

    return total    


print("sum_nums returned", sum_nums([1, 2, 3, 4]))
