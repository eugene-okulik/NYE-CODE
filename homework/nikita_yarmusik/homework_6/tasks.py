text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
updated_words = []

for word in words:
    if word[-1] in ['.', ',']:
        updated_words.append(word[0:-1] + 'ing' + word[-1])
    else:
        updated_words.append(word + 'ing')

print(' '.join(updated_words))


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
