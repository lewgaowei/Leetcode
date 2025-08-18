class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        
        return " ".join(words)


if __name__ == "__main__":
    sol = Solution()  # create an instance
    print(sol.reverseWords("the sky is blue"))     
