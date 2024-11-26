import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def devision(n1, n2):
    return n1 / n2
def multiplication(n1, n2):
    return n1 * n2
def sqr(n1):
    return n1 ** 2
first_num = float(input('What is your first number?: '))
calc = True
while calc:
    operator_ = input("+\n-\n*\n/\n#\nPick an operator: ")
    if operator_ == '#':
        outcome = sqr(first_num)
        print(f'{first_num}^2  = {outcome}')
    second_num = float(input('What is the next number?: '))
    if operator_ == '+':
        outcome = add(first_num, second_num)
        print(f'{first_num} + {second_num} = {outcome}')
    elif operator_ == '-':
        outcome = subtract(first_num, second_num)
        print(f'{first_num} - {second_num} = {outcome}')
    elif operator_ == '/':
        outcome = devision(first_num, second_num)
        print(f'{first_num} / {second_num} = {outcome}')
    elif operator_ == '*':
        outcome = multiplication(first_num, second_num)
        print(f'{first_num} * {second_num} = {outcome}')
    y_or_no = input('if you want to continue print "y", else print "n"'.lower())
    if y_or_no == 'y':
        first_num = outcome
    else:
        calc = False