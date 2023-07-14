class Solution:
    def plusOne(self, digits):
        sums = digits[-1] + 1 
        carry = 1 if sums > 9 else 0 
        digits[-1] = 0 if sums>0 else sums

        for i in range(len(digits)-2, -1, -1):
            if digits[i] + carry > 9 :
                carry = 1
                digits[i] = 0
            else : 
                digits[i] = digits[i] + carry 
                carry = 0

        #if carry == 1:
        #digits.append(1) 
        # return digits [: : -1]

        if carry == 1 : digits.insert(0,1)

        return digits 

digits = [3, 5, 2]
number = Solution()
print(number.plusOne(digits))

"""def boostedDigits(num):
    l = len(num)
    boostedNum = []
    lastDigit = num[l-1]
    
    countNines = 0
    for i in range(l):
        digit = num[i]
        if(digit==9): countNines+=1

    if(lastDigit<9):
        num[l-1] = lastDigit + 1
        boostedNum = num

    elif(countNines==l):
        """for i in range(l):
            boostedNum = 10 * boostedNum"""
        boostedNum = [1]
        for i in range(l):
            boostedNum.append(0)
    else:
        for i in range(l):
            i = l - 1 - i
            digit = num[i]
            if(digit == 9):
                num[i] = 0
            else:
                num[i]+=1
                boostedNum = num
                break

    return boostedNum

#num = [2, 1]
num = [9, 3, 9]
boostedNum = boostedDigits(num)
print(boostedNum)"""