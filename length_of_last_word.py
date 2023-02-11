class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re
        if s.startswith(" ") or s.endswith(" "):

            s = s.strip(" ")
            #print(self.sentence)

        splitted = re.split('\s+', s)
        #print(splitted)
        return len(''.join(splitted[-1:]))

