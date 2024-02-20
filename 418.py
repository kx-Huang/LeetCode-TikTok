class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        for word in sentence:
            if len(word) > cols:
                return 0

        s = ' '.join(sentence) + ' '
        n = len(s)
        ptr = 0
        for i in range(rows):
            ptr += (cols-1)
            # end of col fall on space
            if s[ptr % n] == ' ':
                ptr += 1
            # end of col fall on end of word
            elif s[(ptr+1) % n] == ' ':
                ptr += 2
            # at the mid of the word
            else:
                while ptr > 0 and s[ptr % n] != ' ':
                    ptr -= 1
                ptr += 1
            # at here pointer always at the end of a row

        return ptr // n
