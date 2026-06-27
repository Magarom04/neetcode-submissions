class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        if len(A)>len(B):
            A, B = B, A
        
        total = len(A)+len(B)
        half = (total +1 )//2

        left = 0 
        right = len(A)

        while left <= right :
            partitionA = (left +right)//2
            partitionB = half - partitionA

            Aleft = float("-inf") if partitionA == 0 else A[partitionA -1]
            Aright = float("inf") if partitionA == len(A) else A[partitionA]

            Bleft = float("-inf") if partitionB == 0 else B[partitionB - 1]
            Bright = float("inf") if partitionB == len(B) else B[partitionB] 

            if Aleft <= Bright and Bleft<= Aright :
                if total % 2:
                    return max(Aleft, Bleft)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright :
                right = partitionA - 1
            else : 
                left = partitionA +1
        