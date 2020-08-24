# Time: O(n + m) space: O(n + m) where n is the no. of words in a paragraph and m is no. banned words
from collections import defaultdict
from operator import itemgetter

def mostCommonWord(paragraph, banned):
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

    words = normalized_str.split()

    word_count = defaultdict(int)
    banned_words = set(banned)

    for word in words:
        if word not in banned_words:
            word_count[word] += 1

    return max(word_count.items(), key=itemgetter(1))[0]


paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

result = mostCommonWord(paragraph1, banned)
print(result)