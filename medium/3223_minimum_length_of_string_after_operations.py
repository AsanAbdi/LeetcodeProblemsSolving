class Solution:
    def minimumLength(self, s: str) -> int:
        counter = 0
        while counter < len(s):
            if s[:counter].find(s[counter]) != -1 and s[counter + 1:].find(s[counter]) != -1:
                first = s[:counter].find(s[counter])
                s = s[:first] + s[first + 1:]
                counter -= 1
                if counter < 0:
                    counter = 0
                second = s[counter + 1:].find(s[counter]) + counter + 1
                s = s[:second] + s[second + 1:]
            else:
                counter += 1
        return len(s)