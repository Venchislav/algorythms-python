def short_words(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    return ' '.join([word for word in words if len(word) == minlen])


print(short_words(['hey', 'hi', 'dude', 'wow', 'yes', 'no', 'doom']))
