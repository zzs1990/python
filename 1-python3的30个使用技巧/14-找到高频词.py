# -*- coding: utf-8 -*-
# max() 会返回 list 中的最高值
# test.count 是 list 的内置函数，会统计输入的出现次数
# set(test) 会返回 unique 值
print(f"{'-'*16}找到高频词{'-'*16}")

my_words = [1, 1, 1, 2, 2, 2, 3, 3, 4]
words_set = set(my_words)
word_counts = {}
for word in words_set:
    count = my_words.count(word)
    word_counts[word] = count

max_cnt = max([word_counts[key] for key in word_counts.keys()])
print(f"高频词出现的最大次数为：[{max_cnt}]")

high_freq_word = [key for key in word_counts.keys()
                  if word_counts[key] == max_cnt]
print(f"对应的高频词为：[{high_freq_word}]")

print(f"{'-'*16}找到高频词{'-'*16}")


