num = int(input('Digite um número: '))
print('#' * 14)
for c in range(0, 11):
    print(' {} x {} = {}'.format(num, c, (num * c)))
print('#' * 14)