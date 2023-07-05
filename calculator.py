
# While loop for User to enter two numbers and the operator
while True:
    choice = input('Enter a to perform calculation or b to read from file or c to exit :')
    if choice == 'a':
       # Option a user intends to calculate
        try:
            
            num1 = float(input('Enter a number :'))
            num2 = float(input('Enter another number :'))
            operator= input('Enter an operator(+,-,*,/)')
            if operator == '+':
             result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            
            elif operator == '/':
                try:
                    if num2 == 0:
                      result = num1 / num2 
                except ZeroDivisionError:
            # Inform User that denominator cannot be zero
                 print('Cannot divide by zero')
                
            else:
                raise ValueError('Invalid operator')
                print('Invalid number') 
        # Copy to text file output.txt
            f = open( 'output.txt', 'a')
            f.write (f'{num1} {operator} {num2} = {result}')
            f.close()       

        except ValueError as e:
            print('Error', e)
            
    elif choice == 'b':
       # Ask user for file name option b
       user_input = input('Enter file name :')
       try:
        text_file = open(user_input, 'r')
        print(text_file.read())
       except FileNotFoundError:
        print('File not found')
     # User wants to quit option c
    elif choice == 'c':
       print('Thank you for visiting')
       break
