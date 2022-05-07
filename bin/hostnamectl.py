print('Hello this will help you modify your hostname.')
print('\n')
a = input('What should be the new hostname? ')
with open('etc/hostname', 'w') as f:
    f.write(a)
print('\n')
print('Hostname has been changed!')
exit(0)