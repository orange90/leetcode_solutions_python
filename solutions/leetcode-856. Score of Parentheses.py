class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        left_stack = []
        sum_list = [0] * len(S)
        for i in range(0, len(S)):
            if S[i] == '(':
                left_stack.append(i)
            else:
                left = left_stack.pop()
                if i - left == 1:  # ()
                    sum_list[i] = 1
                else:
                    temp_sum = 2 * sum(sum_list[left:i])
                    sum_list[left:i] = [0] * (i - left)
                    sum_list[i] = temp_sum
        return sum(sum_list)
