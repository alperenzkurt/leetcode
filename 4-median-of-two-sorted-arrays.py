class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        double=False

        if total%2==0:
            mid=total/2
            double=True
        else:
            mid=total//2

        i=0
        prev=0
        curr=0

        while i<mid+1:
            prev=curr
            try:
                n1=nums1[0]
            except:
                n1=float('inf')
            try:
                n2=nums2[0]
            except:
                n2=float('inf')

            if n1 < n2:
                nums1=nums1[1:]
                curr=n1
            else:
                nums2=nums2[1:]
                curr=n2
            i+=1

        if double:
            return (curr+prev)/2
        else:
            return curr
