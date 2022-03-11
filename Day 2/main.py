import numpy

'''solve the problem using division. since we must 
print the product of all places other than itself,
we can multiply them all to find the product of the list
and then divide by itself'''
def solveDivision(line: list):
    nums = []
    for num in line:
        nums.append(int(num))
    product = numpy.prod(nums)
    for i in range(len(nums)):
        nums[i] = int(product/nums[i])
    return nums

'''challenged to do it without division'''
def solveNoDivision(line: list):
    nums = []
    ans = []
    for num in line:
        nums.append(int(num))
    for i in range(len(nums)):
        temp = nums.copy()
        temp.remove(nums[i])
        ans.append(numpy.prod(temp))
    return ans


with open("Day 2/input.txt", 'r') as fin:
    for line in fin:
        print(solveDivision(line.split()))
        print(solveNoDivision(line.split()))
        