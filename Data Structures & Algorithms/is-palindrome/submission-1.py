class Solution:
    def isPalindrome(self, s: str):
        # This is an improved version of my last attempt. This version uses no extra space, so it has O(1) space complexity

        # I'll create *two pointers*, because each one can point to one extremity of s and then we converge them to the middle of the string
        pointerLeft, pointerRight = 0, len(s) - 1

        # To converge them to the middle, I'll use a while loop that runs while the left pointer is still left in relation to the right pointer, that is while pointerLeft is less than pointerRight. In the case wich the string has an odd number of characters, we don't need to check the middle character, because surely it's the same as itself.
        while pointerLeft < pointerRight:
            # Skipping all non-alphanumeric characters
            while pointerLeft < pointerRight and not self.isAlphaNum(s[pointerLeft]):
                pointerLeft += 1
            while pointerLeft < pointerRight and not self.isAlphaNum(s[pointerRight]):
                pointerRight -= 1
            
            if not (s[pointerLeft].lower() == s[pointerRight].lower()):
                return False
            
            # Converge the pointers
            pointerLeft += 1
            pointerRight -= 1
        
        return True
    
    def isAlphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )