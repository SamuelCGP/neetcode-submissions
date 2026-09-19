class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # if it is rotated n times, just do the binary search
        if not nums[left] < nums[right]:
            #binary search for the smallest number (pivot)
            while left < right and not nums[left] < nums[right]:
                mid = (left+right)//2
                if nums[mid] >= nums[left]: left = mid + 1
                else: right = mid #nums[mid] < nums[right]

            #decide if we will search the left or the right sorted side of the array
            if target >= nums[left] and target <= nums[len(nums) - 1]:
                right = len(nums) - 1
            else:
                right = left - 1
                left = 0

        #binary search
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            if nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1