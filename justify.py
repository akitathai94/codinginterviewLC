def reflowLines(maxWidth, words):
    res = []
    # today is 10 
    # words ["today", "is"]
    i = 0
    while i < len(words):
        j = i + 1
        l = len(words[i])
        # put as many as possible words on any line
        while j < len(words) and l + 1 + len(words[j]) <= maxWidth:
            l += 1 + len(words[j])
            j += 1
        
        line = ''
        # left justification
        if j == len(words) or i + 1 == j:
            line += words[i]
            k = i + 1
            while k < j:
                line += '' + words[k]
                k += 1
            while len(line) < maxWidth:
                line += ' '
        else:
            count = j - i - 1
            remain = maxWidth - l + count
            line += words[i]
            k = 0
            while k < remain % count:
                line += '' * (remain // count + 1) + words[i + k + 1]
                k += 1
            while k < count:
                line += '-' * (remain // count) + words[i + k + 1]
                k += 1
        res.append(line)
        i = j
    print (res)

s = 'today is'
lines = s.split(' ')

reflowLines(12, lines)

# test_str = ["It was the best","of time it was","the worst of times"]

# print(test.fullJustify(test_str, 12))