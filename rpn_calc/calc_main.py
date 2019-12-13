from calc_lexer import CalcLexer
from calc_version import *
from math_helpers import *
from collections import namedtuple

import math

"""
.. class:: CalcMain
   :synopsis: The main implementation module for the calculator.

.. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""
class CalcMain:
    def __init__(self, debug=False, verbose=False):
        self.stack = list()
        self.lexer = CalcLexer()
        self.debug = debug
        self.verbose = verbose

    def stack_push(self, term):
        self.stack.append(float(term))

    def stack_pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Error: Stack Underflow")

    def stack_depth(self):
        return len(self.stack)

    def stack_repr(self):
        return ', '.join(map(str, self.stack))

    def check_arity(self, arity):
        if len(self.stack) < arity:
            print(f'Error: Stack arity underflow (wanted {arity}, got {len(self.stack)})')
            return False
        else:
            return True

    def handle_basic_op(self, tok):
        op1 = self.stack_pop()
        op2 = self.stack_pop()

        if tok.type == 'PLUS':
            self.stack_push(op1 + op2)
        elif tok.type == 'MINUS':
            self.stack_push(op1 - op2)
        elif tok.type == 'TIMES':
            self.stack_push(op1 * op2)
        elif tok.type == 'DIV':
            self.stack_push(op1 / op2)

    def handle_function(self, tok):
        if tok.value == 'SIN':
            self.stack_push(math.sin(self.stack_pop()))
        elif tok.value == 'COS':
            self.stack_push(math.cos(self.stack_pop()))
        elif tok.value == 'TAN':
            self.stack_push(math.tan(self.stack_pop()))
        elif tok.value == 'SQRT':
            self.stack_push(math.sqrt(self.stack_pop()))

        elif tok.value == 'EXP':
            base = self.stack_pop()
            exp  = self.stack_pop()
            self.stack_push(math.pow(base, exp))
        elif tok.value == 'NCR':
            rval = self.stack_pop()
            nval = self.stack_pop()
            ncr = MathHelpers.ncr(nval, rval)
            self.stack_push(ncr)
        elif tok.value == 'NPR':
            rval = self.stack_pop()
            nval = self.stack_pop()
            npr = MathHelpers.npr(nval, rval)
            self.stack_push(npr)

    def handle_stackop(self, tok):
        if tok.value == 'DUP':
            n = self.stack_pop()
            self.stack_push(n)
            self.stack_push(n)
        elif tok.value == 'DROP':
            self.stack_pop()
        elif tok.value == 'SWAP':
            x = self.stack_pop()
            y = self.stack_pop()
            self.stack_push(y)
            self.stack_push(x)
        elif tok.value == 'ROLL':
            l = self.stack[:-1]
            l.insert(0, self.stack[-1])
            self.stack = l
        elif tok.value == 'ROLLD':
            l = self.stack[1:]
            l.append(self.stack[0])
            self.stack = l
        elif tok.value == 'DEPTH':
            self.stack_push(self.stack_depth())

    def handle_token(self, tok):
        if tok.type == 'NUMBER':
            self.stack_push(tok.value)
            return True
        elif tok.type in ('PLUS', 'MINUS', 'TIMES', 'DIV'):
            if self.check_arity(2):
                self.handle_basic_op(tok)
            return True
        elif tok.type == 'ARITY1FUNC':
            if self.check_arity(1):
                self.handle_function(tok)
            return True
        elif tok.type == 'ARITY2FUNC':
            if self.check_arity(2):
                self.handle_function(tok)
            return True
        elif tok.type == 'STACKOP':
            self.handle_stackop(tok)
            return True
        return False

    def calculate(self, input_line, result_only=True):
        for tok in self.lexer.tokenize(input_line):
            self.handle_token(tok)
        if result_only:
            return self.stack[-1]
        else:
            RpnCalcResult = namedtuple(RpnCalcResult, ['result', 'stack'])
            r = RpnCalcResult(result=self.stack[-1], stack=self.stack)
            return r


if __name__=="__main__":
    print("The CalcMain class cannot be invoked directly. To run RpnCalc from the\n")
    print("command-line, run the rpn_calc binary. To invoke an interactive RpnCalc\n")
    print("from your own programs, create a CalcRepl() instance and run its repl()\n")
    print("method.")
    exit(0)
