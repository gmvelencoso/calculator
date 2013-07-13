def main():
    exp = raw_input('Input:')
    print(operate(exp))


def operate(string):
    return eval(string)

if __name__ == '__main__':
	main()
