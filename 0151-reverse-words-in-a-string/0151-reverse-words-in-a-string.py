class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        word = ""
        result = []

        for i in range(n-1, -1, -1):
            if s[i] == " ":
                if word:
                    result.append(word[::-1])
                    word = ""
            else:
                word += s[i]

        if word:
            result.append(word[::-1])

        return " ".join(result)