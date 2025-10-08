def patternmatcher(text, pattern):
    found = False
    for i in range(len(text) - len(pattern) + 1):
        found = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            return i
    return -1

print(patternmatcher("abracadabra", "ac"))
print(patternmatcher("how much wood would a woodchuck chuck if a woodchuck could chuck wood?", "woodchuck"))
print(patternmatcher("cat","b"))
print(patternmatcher("cat","t"))
print(patternmatcher('aaab', 'aab'))
print(patternmatcher('abcdef', 'cxe'))
print(patternmatcher('abcdef', 'efx'))
print(patternmatcher('abcabcabdabc', 'abd'))
print(patternmatcher('abcdef', 'abcdefg'))