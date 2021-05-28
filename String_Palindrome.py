# https://www.interviewbit.com/test/b9a83d79a8/?signature=BAhpAxRrEA%3D%3D--fc2973fa80c43d61acc6f8433ed4cc4288c65150#/problem_2
# Three strings A, B, C
# a = substring of A, b = substring of B, c = substring of C
# s = a + b + c , return 1, if there exists some s such that 's' is palindrome else return 0

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def solve(self, A, B, C):
        C = C[::-1]
        l = len(A)
        for i in range(0,l):
            if C.find(A[i]) != -1:
                return 1
        if i >= l-1:
            return 0
