"""
given a string with a ahidden word
print the hidden word
hidden word is POLICE
"""
text = 'QPVWQOVWQLVWQIVWQCVWQEV'
# ind = text.index('P')
# output = ''
# while ind <= len(text):
#     output += text[ind]
#     ind += 4
# print(output)


output = ''
for key, char in enumerate(text):
    if text[key - 1] == 'Q' and text[key + 1] == 'V':
        output += char
print(output)
