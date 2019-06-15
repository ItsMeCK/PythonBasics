a = int(input('Enter number 1'))
b = int(input('Enter number 2'))

try:
    c = a / b
    print("Output::", c)
except Exception as e:
    print("Exception", e)
finally:
    print('Success!!')

