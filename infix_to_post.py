from pythonds.basic.stack import Stack

# define global precendence
class Conversion (object) :
    
    def __init__(self):
        self.prec = {}
        self.init_prec()
        self.op_stack = Stack() #operators will be kept in this stack
        self.output_list = []   #any postfix or prefix expression will be written in the list
        self.token_list = [] #initial expression will be read and kept in this list    
        self.operands = []
        self.init_operand()
        
    def init_prec(self) :
        self.prec["*"] = 3
        self.prec["/"] = 3
        self.prec["+"] = 2
        self.prec["-"] = 2
        self.prec["("] = 1
    
    def init_operand(self) :
        self.operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789"
    
    def re_init(self) :
        #After any operation, the stack should be empty
        self.op_stack = Stack()
        self.output_list = []
        self.token_list = []

    def infixToPostfix(self,infixexpr) :
        '''The function will read an infix expression and write its 
        corresponding expression in the output_list
        doesn't return anything but alters the output_list'''
        self.re_init()
        self.token_list = infixexpr.split()
        for token in self.token_list :
            if token in self.operands :
                self.output_list.append(token)
            elif token == '(' :
                self.op_stack.push(token)
            elif token == ')' :
                top_token = self.op_stack.pop()
                while top_token != '(' :
                    self.output_list.append(top_token)
                    top_token = self.op_stack.pop()
            else :
                while (not self.op_stack.isEmpty()) and \
                    (self.prec[self.op_stack.peek()] >= self.prec[token]) :
                    self.output_list.append(self.op_stack.pop())
                self.op_stack.push(token)    
        while not self.op_stack.isEmpty() :
            self.output_list.append(self.op_stack.pop())             
    
    def getOutput(self) :
        return " ".join(self.output_list)

    def infixToPrefix(self, infixexpr) :
        pass

if __name__=="__main__" :
    test_obj = Conversion()
    test_obj.infixToPostfix("A * B + C * D")
    print test_obj.getOutput()
    test_obj.infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")
    print test_obj.getOutput()
