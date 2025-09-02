#listing_A_1
def find_max_A_1(nums: list[int], n: int) -> int:
    max_number = nums[0]
    for i in range(n):
        if nums[i]>max_number:
            max_number=nums[i]
    return max_number

#listing_A_2
def find_max_A_2(nums: list[int], n: int) -> int:
    return nums[n-1]

#listing_A_3
"""
total = 0
for i in range(n):
    total = total + nums[i]
for i in range(n):
    total = total + nums [i]

"""
#listing_A_$
"""
total = 0
for i in range(n):
    for i in range(n):
        total = total + nums [i]
"""

if __name__ == "__main__":
    NUMBERS = [1,3,8,10,21]
    N = 5
    # print(find_max_A_1(NUMBERS, N))
    print(find_max_A_2(NUMBERS, N))

