#!/usr/bin/env python3

import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
WELCOME_MESSAGE = (
    "Welcome to the RPN calculator!\n"
    "Why do RPN calculators stay so calm? "
    "Because they always know how to handle their operators."
)

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


def get_welcome_message():
    return WELCOME_MESSAGE


def main():
    print(get_welcome_message())
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
