PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


print({
    name: int(price.replace('р', ''))
    for line in PRICE_LIST.split('\n')
    for name, price in [line.rsplit(' ', 1)]
})
