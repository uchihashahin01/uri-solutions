x = input()

count_z = x.count('z')

count_o = x.count('o')

if len(x) <= 20 and x[0] == 'z':
    if (count_o == 2 *count_z):
        print('Yes')
    else:
        print('No')