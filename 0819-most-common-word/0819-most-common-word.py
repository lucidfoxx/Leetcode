class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for char in "!?',;.":
            paragraph= paragraph.replace(char, " ")
        paragraph = " ".join(paragraph.split())
        words = paragraph.lower().split(" ")
        freq = {}
        for word in words:
            if word in banned:
                continue
            if word not in freq:
                freq[word] = 0
            freq[word] += 1

        maxfreq = 0
        maxval = ""
        for i in freq:
            print(i)
            if freq[i] > maxfreq:
                maxfreq = freq[i]
                maxval = i
        return maxval