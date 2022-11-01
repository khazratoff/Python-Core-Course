class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = []
        for i in s:
            l.append(i)
        print(l)
        for i in range(len(l)):
            if l == l[::-1]:
                print(l)
                break
            l.remove(l[i])




solution = Solution()
solution.longestPalindrome('hello')