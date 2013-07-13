def main():
    exp = raw_input('Input:')
    print(operate(exp))

def operate(string):
    # tests if string is an arithmetic expression and only sums or rests
    for i in string:
	if i not in "0123456789+-":
	    return 'Error'

    return eval(string)
	"""Ahora solo opera si son enteros y si se suma o se resta, python lo opera bien
	aunque se le ponga 4--4, que es una operacion correcta."""

if __name__ == '__main__':
    main()
