import argparse
import os

parser = argparse.ArgumentParser(description='Поиск текста в логах')

parser.add_argument('path', type=str, help='Путь к папке с логами')
parser.add_argument('--text', type=str, required=True, help='Текст, который нужно найти в файлах')

args = parser.parse_args()

if not os.path.exists(args.path):
    print(f"Ошибка: путь '{args.path}' не существует.")
    exit(1)

files = os.listdir(args.path)
found = False

for file in files:
    file_path = os.path.join(args.path, file)
    if not os.path.isfile(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line_text in enumerate(f, start=1):
            words = line_text.split()
            for index, word in enumerate(words):
                if args.text.lower() == word.lower():
                    found = True
                    print(f'\nНайдено в файле: {file} (строка {line_number})')
                    print('Контекст:', ' '.join(words[max(0, index - 6): index + 6]))

if not found:
    print("Совпадений не найдено.")
