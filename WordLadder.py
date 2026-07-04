class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) == 1:
            if endWord in wordList:
                return 2
            return 0
        word_set = set(wordList)
        steps = 1
        curr_list = [beginWord]
        chars = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        while len(curr_list) > 0:
            next = []
            steps += 1
            for word in curr_list:
                for i in range(len(word)):
                    for char in chars:
                        new_word = word[:i] + char + word[i + 1 :]
                        if new_word in word_set:
                            if new_word == endWord:
                                return steps
                            next.append(new_word)
            for word in next:
                word_set.discard(word)
            curr_list = next
        return 0
