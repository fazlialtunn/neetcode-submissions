class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        need = len(countT)

        result = [-1, -1]
        resultLen = float("inf")

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if right - left + 1 < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                # remove left character
                c = s[left]
                window[c] -= 1

                if c in countT and window[c] < countT[c]:
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if resultLen != float("inf") else ""