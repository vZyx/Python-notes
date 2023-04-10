while True:
    print('\n\nMenu:')
    print('Enter 1 to sum numbers from 1 to N')
    print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)')
    print('Enter 3 to end the program')

    user_inp = input('\nEnter choice from 1 to 3: ')

    if user_inp != '1' and user_inp != '2' and user_inp != '3':
        print('Invalid Input...Try again')
        continue

    if user_inp == '1':
        n = int(input('Enter a number: '))
        sum = (n * (n+1))//2
        print('Sum from 1 to', n, 'is', sum)
    elif user_inp == '2':
        num1, operation, num2 = input('Enter a simple expression: ').split()
        num1, num2 = float(num1), float(num2)

        # None is a value that means nothing assigned
        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '**':
            result = num1 ** num2
        else:
            # / or //
            if num2 == 0:
                print('Sorry: No way to compute this expression')
            elif operation == '/':
                result = num1 / num2
            else:
                result = num1 // num2

        if result != None:
            print('Expression value is ', result)
    else:
        break