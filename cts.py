import json
from math import *


def getOperation(op):
	if op == "equal":
		return "="
	elif op == "multiply":
		return "*"
	elif op=="add":
		return "+"
	elif op == "subtract":
		return "-"
	else:
		return "/"
	
def getPretty(data):
	if isinstance(data['lhs'],dict):
		lhs = getPretty(data['lhs'])
	else:
		lhs = str(data['lhs'])

	if isinstance(data['rhs'],dict):
		rhs = getPretty(data['rhs'])
	else: 
		rhs = str(data['rhs'])

	return '('+lhs+getOperation(data['op'])+rhs+')'

with open('data.json') as f:
    data = json.load(f)

expression = getPretty(data)[1:-1]

print expression

newstr = expression.replace("(", "")
newstrs = newstr.replace(")", "")

# print newstrs

lens = len(newstrs)

# print newstrs[lens-2]
# for i in range(0,lens):

def isOperand(c):
    if c != "": 
    	return (c in "+-*/")
    else: 
    	return False

def getPriority(c): 
    if c in "+-": 
    	return 0
    if c in "*/": 
    	return 1
    
def isNum(c):
    if c != "": 
    	return (c in "0123456789.")
    else: 
    	return False

def calc(op, num1, num2):
    if op == "+": 
    	return str(float(num1) + float(num2))
    if op == "-": 
    	return str(float(num1) - float(num2))
    if op == "*": 
    	return str(float(num1) * float(num2))
    if op == "/": 
    	return str(float(num1) / float(num2))

def findX(expr):
    expr = list(expr)
    stackChr = list()
    stackNum = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0: 
        	d = expr[0]
        else: 
        	d = ""
        if isNum(c):
            num += c
            if not isNum(d):
                stackNum.append(num)
                num = ""
        elif isOperand(c):
            while True:
                if len(stackChr) > 0: 
                	top = stackChr[-1]
                else: 
                	top = ""
                if isOperand(top):
                    if not getPriority(c) > getPriority(top):
                        num2 = stackNum.pop()
                        op = stackChr.pop()
                        num1 = stackNum.pop()
                        stackNum.append(calc(op, num1, num2))
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                c = stackChr.pop()
                if c == "(":
                    break
                elif isOperand(c):
                    num2 = stackNum.pop()
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))

    while len(stackChr) > 0:
        c = stackChr.pop()
        if c == "(":
            break
        elif isOperand(c):
            num2 = stackNum.pop()
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))
            
    return stackNum.pop()

expr = "2*4+5"
# expr = "(21-1)/10"
print findX(expr)

expr = "(21-1)/10"
# print findX(expr), eval(expr)
# print eval(expr)

# def getX(data):
# 	if isinstance(data['lhs'],dict):
# 		lhs = getX(data['lhs'])
# 	else:
# 		lhs = str(data['lhs'])
# 	if isinstance(data['rhs'],dict):
# 		rhs = getX(data['rhs'])
# 	else: 
# 		rhs = str(data['rhs'])

# 	return lhs+getOperation(rhs+data['op'])


# def getTrans(data):
# 	if isinstance(data['lhs'],dict):
# 		lhs = getTrans(data['lhs'])
# 	else:
# 		lhs = str(data['lhs'])
# 	if isinstance(data['rhs'],dict):
# 		rhs = getTrans(data['rhs'])
# 	else: 
# 		rhs = str(data['rhs'])

# 	return '('+lhs+rhs+ getOperation(data['op'])+')'


# var = getTrans(expression)

# print var

# def oppOp(op):
# 	if op == '+':
# 		return '-'
# 	elif op == '/':
# 		return '*'
# 	elif op == '-':
# 		return '+'
# 	else:
# 		return '/'
