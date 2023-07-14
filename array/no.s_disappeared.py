#448. Leetcode  Find all no.s disappeared 

def disappArray(array):
    nums = set(array)
    l = len(nums)
    disappeared = []

    for num in range(1, l+1):
        if num not in nums:
            disappeared.append(num)

    return disappeared

array = [2, 2, 3, 2]
disappeared = disappArray(array)
print(disappeared)