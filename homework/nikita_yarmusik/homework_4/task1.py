import pprint


dct = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {'1', '2', '3', '4', '5'}
}

print(dct['tuple'][-1])

dct['list'].append('six')
dct['list'].pop(2)

dct['dict'].setdefault('i am a tuple', 1000)
dct['dict'].pop('one')

dct['set'].add('6')
dct['set'].remove('1')

pprint.pp(dct)