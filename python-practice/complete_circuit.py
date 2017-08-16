class LogicGate:

    def __init__(self, name):
        self.label = name
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class UnaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)

        self.pin = None
        
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class AndGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self,name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 and b ==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self,name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b ==1:
            return 1
        else:
            return 0

class XOrGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self,name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==0 or b ==0:
            return 1
        else:
            return 0

class NorGate(UnaryGate):

    def __init__(self,name):
        UnaryGate.__init__(self,name)

    def performGateLogic(self):

        a = self.getPin()
        if a == 0:
            return 1
        else:
            return 0

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


    
             
def main():
    
    a = AndGate("G1")
    b = NorGate("G2")
    connector = Connector(a,b)
    x = b.getOutput()
    print "Outout of NorGate is ", x

main()
