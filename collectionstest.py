#
a=(1,2)
b,c=a
print(b)

#占位符
a=(1,2,3)
b,_,_=a
print(b)

#
a=(1,2,3)
b,*c=a
print(c)

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
import collections
word_counts = collections.Counter(words)
# 出现频率最高的 3 个单词
top_three = word_counts.most_common(3)
print(top_three)

