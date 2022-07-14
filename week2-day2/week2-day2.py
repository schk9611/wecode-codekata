# 최초 풀이
def more_than_half(nums): 
    set_nums = set(nums)
    res      = []
    counts   = 0

    for i in set_nums: 
        if  counts <= nums.count(i): 
            counts = nums.count(i)
            res.append(i)

    return res[-1]


# python의 리스트 함수 중 max의 속성을 이용한 방법
# def more_than_half(nums):
#     res = max(nums, key=nums.count)
#     if nums.count(res) > len(nums) / 2:
#         return res
#     else:
#         return "없습니다!"


# # 과반수의 해당하는 수를 확인하는 가장 빠른 방법
# def more_than_half(nums):
#     for n in set(nums):
#         if nums.count(n) > len(nums)/2:
#             return n 


# 테스트코드
print(more_than_half([3,2,3,3,4,5]))   # 3
print(more_than_half([1,1,1,1,2,2,3,4]))   # 2
print(more_than_half([2,1,2,3,2,6,6,1,2,2,2]))   # 2
print(more_than_half([5,3,5]))   # 5