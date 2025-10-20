from collections import Counter
text = input().lower().split()
word_count = Counter(text)
max_count = max(word_count.values())
result_word = min(word for word, count in word_count.items() if count == max_count)
print(result_word, max_count)
