from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

words_count = Counter(words)
print(words_count)

# 出现次数最多
print(words_count.most_common(3))

# 更新计数
morewords = ['why','are','you','not','looking','in','my','eyes']
words_count.update(morewords)
print(words_count)

print("+" * 80)

# Counter与数学公式
a = Counter(words)
b = Counter(morewords)

print(a)
print(b)

print(a+b)
print(a-b)
