"""
TREE STRUCTURE:

                    left   (NodeInt or NodeBinaryOp)
                 /
        operator 
                 \   
                    right  (NodeInt)

""" 



def main():
    input = raw_input('Input:')
    print(operate(input))

def test():
    operations = ["10", "3+4", "10-3+2", "123-321+43-12", "123-1-2-3"]
    values = [10, 7, 9, -167, 117]
    print("Automatic tests")
    for i in range(len(values)):
        if values[i] == operate(operations[i]):
            print "PASS %s = %s" % (operations[i], values[i])
        else:
            print "FAIL {0} != {1} ({2})".format(operations[i], values[i], operate(operations[i]))


#tokenizes the string to obtain a list of nodes
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []
    
    while buffer.peek():
        token = None
        #tries with every type of token
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        #if there is no token, means there is no input
        if not token:
            raise ValueError("Error in syntax")
    
    return tokens


def parse(tokens):
    if tokens[0][0] != 'int':
        raise ValueError("Must start with an int")
    #now tokens[0] is an int
    node = NodeInt(tokens[0][1])    #saves the first token value
    nbo = None
    last = tokens[0][0]             #saves the first token type
    #starts with the second token
    for token in tokens[1:]:
        if token[0] == last:
            raise ValueError("Error in syntax")
        last = token[0]
        #if it's an operator, saves it at nbo, and the last int at nbo.left
        if token[0] == 'ope':
            nbo = NodeBinaryOp(token[1])
            nbo.left = node    
        #if it's an int, saves it at nbo.right
        if token[0] == 'int':
            nbo.right = NodeInt(token[1])
            node = nbo
    
    return node
    
def calculate(nbo):    
    #if it's a Binary Operator Node calculates the result of its operation
    if isinstance(nbo.left, NodeBinaryOp):
        leftval = calculate(nbo.left)
    else:
        leftval = nbo.left.value
    #calculates the result of the operation    
    if nbo.kind == '-':
        return leftval - nbo.right.value
    elif nbo.kind == '+':
        return leftval + nbo.right.value
    else:
        raise ValueError("Wrong operator")

def evaluate(node):
    #if it's only an int without operators
    if isinstance(node, NodeInt):
        return node.value
    else:
        return calculate(node)
    

def operate(string):
    #tokenizes the input string
    tokens = tokenize(string)
    #parses the token list to a tree
    node = parse(tokens)
    
    return evaluate(node)
    
        
#defines Node classes to create the tree
class Node(object):
    pass
#defines Int Node with a value (int)     
class NodeInt(Node):
    def __init__(self, value):
        self.value = value
#defines a Binary Operator Node with a value (+ or -)
class NodeBinaryOp(Node):
    def __init__(self, kind):
        self.kind = kind
        self.left = None    #left node
        self.right = None   #right node     
    
#define Token classes    
class Token(object):
    def consume(self, buffer):
        pass
#tokenizer for int
class TokenInt(Token):
    #reads the buffer while char are numbers
    def consume(self, buffer):
        accum = ""
        while True:
            ch = buffer.peek()
            if ch is None or ch not in "0123456789":
                break
            else:
                accum += ch
                buffer.advance()
        #if its not empty returns the type and the value         
        if accum != "":
            return ("int", int(accum))
        else:
            return None 

class TokenOperator(Token):
    #reads the buffer only one position and returns the type and the value of the operator or None
    def consume(self, buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-":
            buffer.advance()
            return ("ope", ch)
        return None
        
#define buffer to read the input string     
class Buffer(object):
    #String data: the input string
    def __init__(self, data):
        self.data = data
        self.offset = 0
    #returns the char in the offset position of the string
    def peek(self):
        #if its the last one returns none
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]
    #advances one position of the cursor    
    def advance(self):
        self.offset += 1
        

if __name__ == '__main__':
    #main()
    test()
