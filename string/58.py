# LeetCode Problem: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy

def lengthOfLastWord(s):
    r = len(s) - 1
    count = 0

    # Trim trailing spaces
    while r >= 0 and s[r] == " ":
        r -= 1

    # Count characters until the next space
    while r >= 0 and s[r] != " ":
        count += 1
        r -= 1

    return count

# Example
s = "fly me   to   the moon  "
print(lengthOfLastWord(s))  # Output: 4
