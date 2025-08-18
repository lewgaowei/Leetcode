from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        g = gcd(len(str1), len(str2))
        print(g)
        return str1[:g]
    

if __name__ == "__main__":
    sol = Solution()  # create an instance
    print(sol.gcdOfStrings("ABABAB", "ABAB"))     
    
    

"""
Time = O(n+m)

Space = O(n+m)
"""