#!/usr/bin/env python3

import operator, string

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}

def calculate(arg):
    st = []
    for sign in arg.split():
        if sign in ops:
            y,x = st.pop(), st.pop()
            z = ops[sign](x,y)
        else: 
            z = int(sign)
        st.append(z)
    return(st.pop())        
def main():
    while True: 
        calculate(input("rpn calc> "))
        

if __name__ == '__main__':
    main()
