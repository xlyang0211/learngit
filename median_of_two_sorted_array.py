#This problem is very difficult to solve!
http://blog.csdn.net/yutianzuijin/article/details/11499917/
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        ab_m = (len(A) + len(B) + 1) / 2
        flag = 0
        if (len(A)+len(B)) % 2 == 0:
            flag = 1
        a_m = 0
        b_m = 0
        a_flag = 0
        b_flag = 0
        if len(A) == 0 and len(B) != 0:
            if flag == 1:
                return float((B[ab_m-1]+B[ab_m]))/2
            else:
                return float(B[ab_m-1])
        elif len(B) == 0 and len(A) != 0:
            if flag == 1:
                return float((A[ab_m-1]+A[ab_m]))/2
            else:
                return float(A[ab_m-1])
        elif len(A) == 1 and len(B) == 1:
            return float(A[0]+B[0])/2
        while ab_m > 1:
            if len(A) <= ab_m / 2:
                a_m = len(A)
                a_flag = 1
            else:
                a_m = ab_m / 2
            if len(B) <= ab_m / 2:
                b_m = len(B)
                b_flag = 1
            else:
                b_m = ab_m / 2
            if a_flag == 1:
                if flag:
                    return float((B[ab_m - len(A)-1] + B[ab_m - len(A)]))/2
                else:
                    return float(B[ab_m - len(A)-1])
            elif b_flag == 1:
                if flag:
                    return float((A[ab_m - len(B)-1] + A[ab_m - len(B)]))/2
                else:
                    return float(A[ab_m - len(B)-1])
            elif A[a_m-1] == B[b_m-1]:
                A = A[a_m:]
                B = B[b_m:]
                ab_m -= a_m
                ab_m -= b_m
            elif A[a_m-1] < B[b_m-1]:
                A = A[a_m:]
                ab_m -= a_m
            else:
                B = B[b_m:]
                ab_m -= b_m
        if A[0] < B[0]:
            if flag:
                return float((A[0] + A[1]))/2
            else:
                return float(A[0])
        else:
            if flag:
                return float((B[0] + B[1]))/2
            else:
                return float(B[0])

if __name__ == "__main__":
    A = [1, 4, 9, 15, 20, 50, 444, 1000]
    B = [2, 54, 295, 333, 553, 554, 555]
    a = []
    b = [2, 3]
    solution = Solution()
    print solution.findMedianSortedArrays(b, a)