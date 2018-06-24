class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        if A == B:
            if len(set(list(A))) < len(A):  # exist duplication
                return True
            else:
                return False
        i = 0
        differnt_A = []
        differnt_B = []
        while i < len(A):
            if A[i] != B[i]:
                differnt_A.append(A[i])
                differnt_B.append(B[i])
                if len(differnt_A) > 2:
                    return False
            i += 1

        if len(differnt_A) < 2:
            return False
        if differnt_A[0] == differnt_B[1] and differnt_A[1] == differnt_B[0]:
            return True
        else:
            return False