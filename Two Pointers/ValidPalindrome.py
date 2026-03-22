

"""Check if a string is a palindrome, considering only alphanumeric characters and ignoring cases."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters at left and right pointers
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_string = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(test_string))  # Output: True