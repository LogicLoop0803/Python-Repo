class Solution:
    def searchRange(nums, target):
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            if nums[mid]==target:
                k = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            k = -1
        if k == -1:
            return [-1,-1]
        else:
            if k==0:
                right=k
                left_count = 0
                right_count = 0
                while nums[k]==nums[right]:
                    right+=1
                    right_count+=1
            elif k==len(nums)-1:
                left = k
                right_count = 0
                left_count = 0
                while nums[k]==nums[left]:
                    left-=1
                    left_count+=1
            else:
                right = k
                left = k
                right_count = 0
                left_count = 0
                while nums[k]==nums[right]:
                    right+=1
                    right_count+=1
                while nums[k]==nums[left]:
                    left-=1
                    left_count+=1
        return([k-left_count,k+right_count])
