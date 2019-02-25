from itertools import chain, combinations

def Cardinal(elem):
    print()
    print(' '*20)
    print('Crdnlty is :')
    print(len(set(elem)))

def powset(iterable):
    gam = list(iterable)
    res = chain.from_iterable(combinations(gam, z) for z in range(len(gam)+1))

    print()
    print(' ' * 20)
    print('Powset is :')

    for subset in res:
        print(subset)


elem = []
ele_number = input('Number of elements: ')

for num in range(int(ele_number)):
    int_elem = input('Elemt {}: '.format(num + 1))

    elem.append(int_elem)


while True:
    print()
    print(' ' * 20)
    print('1.Crdnlty')
    print('2.Powset')
    print('3.Ext')

    sel = input('Slct: ')


    if sel == '1':
        Cardinal(elem)


    elif sel == '2':
        powset(elem)


    elif sel == '3':
        exit()

    else:
        print('\nInvalid choice')
