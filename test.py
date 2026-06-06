word1 = "abcd"
word2 = "pq"

result = ""

len1 = len(word1)
len2 = len(word2)

max_len = max(len1, len2)

for i in range(max_len):
    if i<len1:
        result += word1[i]
    if i<len2:
        result += word2[i]
    
print(result)