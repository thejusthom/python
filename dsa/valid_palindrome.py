# s = "A man, a plan, a canal: Panama"
s = "race a car"
front = 0
back = len(s) - 1
# for _ in range(back):
#     if front < back:
#         if s[front].isalnum():
#             if s[back].isalnum():
#                 if s[front].lower() == s[back].lower():
#                     back -= 1
#                     front += 1
#                 else:
#                     print ("False")
#             else:
#                 back -= 1
#         else:
#             front += 1
# print("True")    

class Solution:
    def isPalindrome(self,s:str) -> bool:
        right, left = 0, len(s) - 1
        while left < right:
            if left < right and not self.isAlpaNum(s[left]):
                left += 1
            if left < right and not self.isAlpaNum(s[right]):
                right += 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right += 1
        return True
    
    def isAlpaNum(self,c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
    
print(Solution().isPalindrome("race a car")) 
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))