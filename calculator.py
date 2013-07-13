def main():
    exp = raw_input('Input:')
    print(operate(exp))


def operate(string):
    try:
	return eval(string)
    except:
	return 'Error'

if __name__ == '__main__':
	main()
