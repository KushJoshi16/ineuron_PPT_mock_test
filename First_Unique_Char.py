'''
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.

'''


def firstUniqChar(s: str) -> int:
    '''
    Function to find the first non-repeating character and return its index.
    If no non-repeating character is found it returns -1
    '''
    s_chr = {}
    chrs = set()
    n = len(s)

    for i in range(n-1,-1,-1):
        if s[i] not in s_chr:
            s_chr[s[i]] = i
        else: continue
        
    for i in range(n):
        if s[i] not in chrs and s_chr[s[i]] == i:
            return i
        chrs.add(s[i])

    return -1


if __name__ == "__main__":

    ind1 = firstUniqChar("leetcode")
    print(ind1)

    ind2 = firstUniqChar("loveleetcode")
    print(ind2)

    ind3 = firstUniqChar("aabb")
    print(ind3)
    

            