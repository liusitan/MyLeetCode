#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
import random
from typing import List
import unittest as ut

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        quickSort(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        

# BUbble sort
def bubbleSort(nums:List[int]) -> List[int]:
    l = len(nums)
    for i in range(l):
        minid = i
        for j in range(i,l):
            if nums[j] < nums[minid]:
                minid = j
        nums[i],nums[minid] = nums[minid],nums[i]  
    return nums
def insertionSort(nums:List[int])->List[int]:
    l = len(nums)
    for i in  range(1,l):
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j-1],nums[j] = nums[j], nums[j-1]
            else:
                break
    return nums

def mergeSort(nums:List[int]) -> List[int]:
    def merge(a1:List[int], a2:List[int]) -> List[int]:
        i1 = 0
        i2 = 0
        l1 = len(a1) if a1!= None else 0
        l2 = len(a2) if a2!=None else 0
        res = []
        try:
            while i1 < l1 or i2 < l2:
                if i1>=l1:
                    e1 = float('inf')
                else:
                    e1 = a1[i1]
                if i2>=l2:
                    e2 = float('inf')  
                else:
                    e2= a2[i2]
                if e1 < e2:
                    res.append(e1)
                    i1+=1
                else:
                    res.append(e2)
                    i2+=1
        except IndexError:
            print(IndexError.args)
        return res
                
    def sort(nums:List[int])->List[int]:
        l = len(nums)
        if l == 1:
            return nums
        m = l//2
        nums = merge(sort(nums[:m]),sort(nums[m:]))
        return nums
    return sort(nums)

def quickSort(nums:List[int])->List[int]:
    def sort(nums:List[int], lend, rend):
        if (rend -lend) <=1:
            return
        if lend < len(nums):
            l = lend
            p = nums[lend]

            r = rend - 1
            while l < r:
                while(l < r and nums[r] > p):
                    r-=1
                if l < r:
                    nums[l] = nums[r]
                    
                while(l< r and nums[l] <= p):
                    l+=1
                if l < r:
                    nums[r] = nums[l]
            nums[l] = p
            sort(nums,lend,r)
            sort(nums,r+1,rend)
    sort(nums,0,len(nums))   
    return nums

    
def assertEqual(n1:List[int],n2:List[int])->bool:
    if len(n1 ) != len(n2):
        return False
    for i, j in zip(n1,n2):
        if i!= j:
            return False
    return True
def genRandomList():
    randomlist = []
    for i in range(0,30):
        n = random.randint(1,30)
        randomlist.append(n)
    return randomlist
testset = []
for i in range(100):
    testset.append(genRandomList())

# print("bubble sort test")
# for t in testset:
#     rt = t.copy()
#     if not assertEqual(bubbleSort(rt),sorted(t)):
#         print(t)
#         print(sorted(t))
#         print(bubbleSort(rt))
#         print("bubble sort failure")
#         break


# print("insertion sort test")
# for t in testset:
#     rt = t.copy()
#     if not assertEqual(insertionSort(rt),sorted(t)):
#         print(t)
#         print(sorted(t))
#         print(insertionSort(rt))
#         print("insertion sort failure")
#         break
# print("merge sort test")
# for t in testset:
#     rt = t.copy()
#     if not assertEqual(mergeSort(rt),sorted(t)):
#         print(t)
#         print(sorted(t))
#         print(mergeSort(rt))
#         print("merge sort failure")
#         break

print("quicksort test")
for t in testset:
    rt = t.copy()
    if not assertEqual(quickSort(rt),sorted(t)):
        print(t)
        print(sorted(t))
        print(quickSort(rt))
        print("quick sort failure")
        break
# @lc code=end

