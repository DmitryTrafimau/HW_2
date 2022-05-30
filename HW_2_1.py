a = 4
b = a
c = b
print(id(a))
print(id(b))
print(id(c),'\n')

x = [6]
y = [6]
print(id(x))
print(id(y),'\n')

a = [4]
b = [a]
c = [b]
print(id(a))
print(id(b))
print(id(c),'\n')

x = [6]
y = x
print(id(x))
print(id(y),'\n')


s = input ('Введите произвольную строку ')
s_even = (s[1::2])
s_odd = (s[::2])
print('''Введенная строка - ''',s.strip(),'''\n\n''', sep='''"''')
print(s_even.strip(),'''   ''',s_odd.strip(),'\n','!!!')
