#representation of a logic gate 

import os
import sys

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getlabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        ''' As we inherit from the class LogicGate, we initialize the subclass with
        the initialization method from the inherited class.
        Child class constructors need to call parent class constructors and then move 
        on to their own distinguishing data. super which can be used in place of explicitly 
        naming the parent class. 
        '''
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getlabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getlabel()+"-->"))

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        
        self.pin = None
    
    def getPin(self):
        return int(input("Enter pin input for gate "+ self.getlabel()+"-->"))

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        return (a*b)

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
  
    def performGateLogic(self):
  
        a = self.getPinA()
        b = self.getPinB()
        if a*b == 0:
            return 0
        else :
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        return (1-a)
    

if __name__=="__main__":
    #    AndGate1 = AndGate('AND')
    #    print AndGate1.performGateLogic()
    
    #OrGate1 = OrGate('OR')
    #print OrGate1.performGateLogic()
    
    OrGate1 = OrGate('OR')
    print OrGate1.performGateLogic()
    
    OrGate2 = OrGate('OR')
    print OrGate2.performGateLogic()
    NotGate1 = NotGate('NOT')
    print NotGate1.performGateLogic()
