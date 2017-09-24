# def isPalindrome(x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         len_x = len(str(x)) 
#         i = 0
#         flag = True
#         while(i<len_x/2):
#             if str(x)[i] != str(x)[len_x-1-i]:
#                 flag = False
#                 break
#             i += 1    
    
#         return flag

# print(isPalindrome(-1))


# # The line "without using extra space" is what threw me off.
# # My solution is unnecessarily complicated
# # Remember to recongnize the problem and the disguise.
# def isPalindrome(x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if str(x) == str(x)[::-1]:
#             return True
#         else:
#             return False

# # This is even cleaner. Day.
def isPalindrome(self, x):
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]

def isPalindrome(x):
    if x < 0 or (x%10==0 and x!=0):
        return False

    reversed_int = 0

    while(x > reversed_int):
        reversed_int = reversed_int * 10 + x%10
        x /= 10
        print reversed_int

    return x == reversed_int or x == reversed_int/10

print(isPalindrome(12321))


