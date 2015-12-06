# coding:utf-8


def cal(s):
    numA=float(raw_input('please enter a number'))
    op=raw_input('please enter a operator:')
    numB=float(raw_input('Please enter another number: '))
    if op == '+':
        print "result: ",numA+numB
    elif op == '-':
        print "result: ",numA-numB
    elif op == '*':
        print "result: ",numA*numB
    elif op == '/':
        print "result: ",numA/numB
    elif op=='**':
        print"result:",numA**numB
    else:
        print "Unknown operator ",op

