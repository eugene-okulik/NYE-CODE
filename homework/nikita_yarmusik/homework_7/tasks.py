def ask_number(correct_number=1):
    print("Введите число:")

    while True:
        response = input()

        if not response.isdigit():
            print("Введите число!")
            continue

        number = int(response)
        if number == correct_number:
            print("Вы угадали!")
            break
        else:
            print("Попробуйте еще раз!")


ask_number(2)


words = {"I": 3, "love": 5, "Python": 1, "!": 50}


def call_value(your_words):
    for key, value in your_words.items():
        print(key * value)


call_value(words)


def update_text(your_text):
    return int(your_text[your_text.index(":") + 1 :]) + 10


print(update_text("результат операции: 42"))
