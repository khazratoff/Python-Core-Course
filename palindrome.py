class Solution:


    def isPalindrome(self, number)->bool:
      l = []
      if number>0:
        while number > 0 :
            digit = number % 10
            l.append(digit)
            number =  number // 10
        if l == l[::-1]:
            return True
        else:
            return False 
      else:
        return False


s = Solution()
n = int(input("Input number: "))
print(s.isPalindrome(n))
