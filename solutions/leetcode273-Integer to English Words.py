class Solution(object):
    small_nums = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    ty_s = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    large_amount = ['', ' Thousand', ' Million', ' Billion']

    def numberToWords(self, input_num):
        """
        :type input_num: int
        :rtype: str
        """
        if input_num < 20:
            return self.small_nums[input_num]

        elif input_num < 100:
            return self.ty_s[input_num // 10] + (
            (' ' + self.small_nums[input_num % 10]) if (input_num % 10 > 0) else '')

        elif input_num < 1000:
            return self.small_nums[input_num // 100] + ' Hundred' + (
            ' ' + self.numberToWords(input_num % 100) if (input_num % 100 > 0) else '')
        else:
            acc = ''
            i = 0
            while input_num > 0:
                front = input_num % 1000
                acc = (self.numberToWords(front) + self.get_unit(i) + (
                ' ' if len(acc) > 0 else '') + acc) if front > 0 else acc
                input_num = input_num // 1000
                if input_num == 0:
                    break
                i += 1
            return acc

    def get_unit(self, num):
        return self.large_amount[num]