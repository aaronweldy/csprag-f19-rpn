#!/usr/bin/env python3

import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
EXIT_COMMANDS = {"exit", "q", "quit"}


def calculate(arg):
    st = []
    for sign in arg.split():
        if sign in ops:
            y, x = st.pop(), st.pop()
            z = ops[sign](x, y)
        else:
            z = int(sign)
        st.append(z)
    return st.pop()


def should_quit(arg):
    return arg.strip().lower() in EXIT_COMMANDS


def main():
    while True:
        try:
            user_input = input("rpn calc> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if should_quit(user_input):
            print("Goodbye!")
            break

        print(calculate(user_input))


if __name__ == '__main__':
    main()
