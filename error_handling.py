try:
    f = open('testfile.py', 'r')
    f.write('Write a test line.')
except OSError:
    print('You have an OS error.')
finally:
    print('Finished running.')

# try:
    # block of code program tries to run
# except: # can specify an error or leave blank to catch all errors
    # if there's an error, this block of code runs
# else:
    # if there's no error, this code will run
# finally:
    # this code will always run at the end


try:
    for i in ['a', 'b', 'c']:
        print(i**i)
except:
    print("Type error. You can't square a string.")
finally:
    print('End.')

try:
    x = 5
    y = 0
    z = 5/0
except ZeroDivisionError:
    print('Zero division error. You cannot divide by zero.')
finally:
    print('End.')


def ask_for_interger():
    while True:
        try:
            result = int(input('Please provide a whole number. '))
        except:
            print('An error occurred. Please try again.')
            continue
        else:
            print("Your number squared is: ", result ** 2)
            break
