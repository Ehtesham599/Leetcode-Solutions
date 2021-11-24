class Solution:
    def is_positive_or_negative(self, sign, num):
        """This Method add the sign of the number cheks the first char if `-` or `+` to give the sign to the number"""
        if sign == '-':
            negative_num = -int(num)
            return negative_num
        elif sign == '+':
            positive_num = +int(num)
            return positive_num
        else:
            return num
        
    def check_final_result_within_range(self,num):
        """This method checks the given number if it is within the range [-231, 231 - 1],
        if less than the negative range, result is clamped to -2**31
        if greater than the positive range, result is clamped to (2**31)-1
        
        args:
        -----
        
        num: integer number can be positive or negative (eg: -233)
        """
        MIN_INT = -2**31
        MAX_INT = (2**31)-1
        res = int(num)
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
        
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        whitespace = ""
        sign=""
        digit_from_num=[]
        num=[]
        result=""
        if s:
            # Read in and ignore any leading whitespace
            if s[0] == " ":
                whitespace = s[0]
            s_remove_whitespace = s.strip()
            
            if s_remove_whitespace:
                # Check if the next character in `s_remove_whitespace` is '-' or '+',
                # if `-` or `+`, store it in `sign` and the rest charactors in `num`
                if s_remove_whitespace[0] in ['-','+']:
                    sign = s_remove_whitespace[0]
                    num = s_remove_whitespace[1:]
                else:
                    num = s_remove_whitespace
                    
                # Read in next the characters until the next non-digit character
                # if `num` has non-digit return 0 otherwise fetch only the first_digits and check if digits fit in range [-2^31, 2^31 - 1]
                if num.isnumeric():
                    new_num = self.is_positive_or_negative(sign, num)
                    final_result_num = self.check_final_result_within_range(new_num)
                    return final_result_num
                else:
                    for digit in num:
                        if digit.isnumeric():
                            digit_from_num.append(digit)
                            
                        elif not digit.isnumeric():# if not digit ignot the rest
                            break
                                         
                    if len(digit_from_num)>0:
                        for int_num in digit_from_num:
                            result += int_num
                            
                        if result:
                            final_result =  self.is_positive_or_negative(sign, result)
                            final_result_num = self.check_final_result_within_range(final_result)
                            return final_result_num  
        return 0
        