from pythonds.basic.stack import Stack

def parChecker(String) :
    '''read a string and check whether it has balanced parathesis'''
    s = Stack()
    balance = True
    for char in String : 
        if char == '(' :
            s.push(char)
        elif char != ')' :
            pass
        elif char == ')' :
            if s.isEmpty() :
                balance = False
            else :
                s.pop()
    return balance

if __name__=='__main__' :
    a = parChecker('(jisaji90()))')
    b = parChecker('()jojojo')
    c = parChecker(')))(jiji')
    d = parChecker('(a)(8)()')
    print a
    print b
    print c
    print d
