class Solution:
    def isPalindrome(self, s: str):
        # First, I'll remove spaces and non-alphanumeric characters since they don't count when evaluating if s is a palindrome or not
        s = s.replace(" ", "")
        s = ''.join(filter(str.isalnum, s))
        # Since palindromes are case-insensitive, we'll need to assure all letters are on the same capitalization to make the checks easier
        s = s.lower()

        # Then, I'll create *two pointers*, because each one can point to one extremity of s and then we converge them to the middle of the string
        pointerLeft = 0
        pointerRight = len(s) - 1

        # To converge them to the middle, I'll use a while loop that runs while the left pointer is still left in relation to the right pointer, that is while pointerLeft is less than pointerRight. In the case wich the string has an odd number of characters, we don't need to check the middle character, because surely it's the same as itself.
        while pointerLeft < pointerRight:
            if not (s[pointerLeft] == s[pointerRight]): return False
            pointerLeft += 1
            pointerRight -= 1
        
        return True