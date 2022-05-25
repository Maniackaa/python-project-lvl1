bar_char = 'P'
s = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 10, 10, 20)
k = list(s)
sym = bar_char
bash = sym + sym


k.__str__
k.sort()
for i in range(0, len(k)):
    k[i] = str(k[i])

#  Находим номиналы монет
nominals_of_monets = ['1', '2', '3', '5', '10', '15', '20']
#  print(nominals_of_monets)

stack_mon = []
for i in range(0, (len(nominals_of_monets))):
    if nominals_of_monets[i] in k:
        stack_mon.append(str(nominals_of_monets[i]))
#  print('stack_mon', stack_mon)

stack = [[]]
for i in range(0, len(stack_mon) - 1):
    stack.append([])

#  print('stack ', stack)

count_nom = [0] * len(stack_mon)
for i in range(0, len(stack_mon)):
    count_nom[i] = k.count(stack_mon[i])
#  print('count_nom ', count_nom)

for i in range(0, len(stack_mon)):
    for line in range(0, max(count_nom) + 1):
        if count_nom[i] > line:
            stack[i].append(bash)
        elif count_nom[i] == line:
            stack[i].append(str(count_nom[i]) + '-')
        elif count_nom[i] < line:
            stack[i].append('++')

for x in range(max(count_nom), -1, -1):
    for i in range(0, len(stack_mon)):
        print('%2s' % stack[i][x], end=' ')
    print()

print('-' * (3 * len(stack_mon) - 1))

for i in range(0, len(stack_mon)):
    print('%-2s' % stack_mon[i], end=' ')
