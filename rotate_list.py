def rotate_list(nums: list, steps: int) -> list:
    rotated_list = nums[-steps:] + nums[:-steps]
    return rotated_list

print(rotate_list(nums=[-1, -100, 3, 99], steps = 2))
