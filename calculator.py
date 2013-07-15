def main():
    input = raw_input('Input:')
    print(operate(input))

def test():
    operations = ["10","3+4","10-3+2","123-321+43-12","123-1-2-3"]
    values = ["10","7","9","-167","117"]
    print("Automatic tests")
    for i in range(0,5):
        print "Expected:",values[i],"\tReceived:",operate(operations[i]),"\t(",operations[i],")" 
    

def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []
    
    while buffer.peek():
        token = None
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        
        if not token:
            raise ValueError("Error in syntax")
    
    return tokens


def parse(tokens):
    if tokens[0][0] != 'int':
        raise ValueError("Must start with an int")
    #now tokens[0] is an int
    node = NodeInt(tokens[0][1])   
    nbo = None
    last = tokens[0][0]
    
    for token in tokens[1:]:
        if token[0] == last:
            raise ValueError("Error in syntax")
        last = token[0]    
        
        if token[0] == 'ope':
            nbo = NodeBinaryOp(token[1])
            nbo.left = node    
        
        if token[0] == 'int':
            nbo.right = NodeInt(token[1])
            node = nbo
    
    return node
    
def calculate(nbo):    
    if isinstance(nbo.left, NodeBinaryOp):
        leftval = calculate(nbo.left)
    else:
        leftval = nbo.left.value

    if nbo.kind == '-':
        return leftval - nbo.right.value
    elif nbo.kind == '+':
        return leftval + nbo.right.value
    else:
        raise ValueError("Wrong operator")

    
def operate(string):
    #tokenizes the input string
    tokens = tokenize(string)
    #parses the token list to a tree
    node = parse(tokens)
    
    if isinstance(node, NodeInt):
        return node.value
    else:
        return calculate(node)
        
#define Node classes to create the tree
class Node(object):
    pass
    
class NodeInt(Node):
    def __init__(self, value):
        self.value = value

class NodeBinaryOp(Node):
    def __init__(self, kind):
        self.kind = kind
        self.left = None
        self.right = None        
    
#define Token classes    
class Token(object):
    def consume(self, buffer):
        pass

class TokenInt(Token):
    def consume(self, buffer):
        accum = ""
        while True:
            ch = buffer.peek()
            if ch is None or ch not in "0123456789":
                break
            else:
                accum += ch
                buffer.advance()
                
        if accum != "":
            return ("int", int(accum))
        else:
            return None 

class TokenOperator(Token):
    def consume(self, buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-":
            buffer.advance()
            return ("ope", ch)
        return None
        
#define buffer to read the input        
class Buffer(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    
    def peek(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]
        
    def advance(self):
        self.offset += 1
        

if __name__ == '__main__':
    #main()
    test()
