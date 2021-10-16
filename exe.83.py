expr = str(input('Digite um expressão: '))
list = []
for simp in expr:
    if simp == '(':
        list.append('(')
    elif simp == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
if len(list) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão não esta valida')