# 数组/字符串

"""
1.
给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution1:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### your code ###
        
        # idea:双指针法
        nums = nums1.copy()
        i = 0
        j = 0
        while not(i==m or j==n):
            if nums[i] > nums2[j]: 
                nums1[i+j] = nums2[j]
                j+=1
            else:
                nums1[i+j] = nums[i]
                i+=1
            # print(nums)
        if i!=m and j==n:nums1[i+j:] = nums[i:m]
        elif j!=n and i==m:nums1[i+j:] = nums2[j:n]
        
        ### your code ###
        print(nums1)
        
class Solution1_:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 逆向双指针，排序最大的在nums1的后面，这样一来可以节省空间复杂度
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
            
            
"""
2.
"""

        
if __name__ == "__main__":
    test = Solution1()
    test.merge(nums1=[1,0],m=1,nums2=[2],n=1)