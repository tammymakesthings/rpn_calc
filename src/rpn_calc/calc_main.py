from collections import namedtuple

import math

"""
.. module:: rpn_calc
    :synopsis: Simple RPN calculator with a sly-based parser.

    .. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""

class CalcMain:
    """The main class for the rpn_calc calculator.

    This class handles tokenizing of input strings, stack management, and
    calculation of results. It implements the processing of all input tokens
    except for those of the ``INLINE_CMD`` type, which are handled in the
    REPL class instead.

    To use the calculator, create an instance of this class and then pass
    strings of RPN commands to the ``calculate`` method. The calculator's
    stack is maintained as an instance variable, so multiple calls to
    ``calculate`` will use the same stack."""


    def __init__(self, debug=False, verbose=False):
        """Create a new instance of the calculator.

        args:
            debug (bool):   If true, debugging output about parsing operations
                            will be printed.
            verbose (bool): If true, the stack contents will be printed after
                            each ``calculate`` operation."""

        self.stack = list()
        self.lexer = CalcLexer()
        self.debug = debug
        self.verbose = verbose


    def stack_push(self, term):
        """Push a number onto the stack. Numbers will be converted to float
        before being pushed onto the stack.

        args:
            term (float):   The number to push onto the stack."""
        self.stack.append(float(term))


    def stack_pop(self):
        """Pop a number from the stack. If the stack is empty, an error
        message will be printed and ``None` will be returned.

        returns:
            float:  The number popped from the stack. ``None`` is returned if
                    the stack is empty."""
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Error: Stack Underflow")
            return None


    def stack_depth(self):
        """Return the current stack depth.

        returns:
            int:    The current stack depth."""
        return len(self.stack)


    def stack_repr(self):
        """Return a string representation of the contents of the stack.

        returns:
            str:    The current contents of the stack, in human-readable form."""
        return ', '.join(map(str, self.stack))


    def check_arity(self, arity):
        """Check that the stack contains enough elements to perform an operation.

        args:
            arity (int):    The number of elements needed for the next operation

        returns:
            bool:   True if the stack contains enough elements to satisfy the
                    operation, False (and prints an error) otherwise."""
        if len(self.stack) < arity:
            print(f'Error: Stack arity underflow (wanted {arity}, got {len(self.stack)})')
            return False
        else:
            return True


    def handle_basic_op(self, tok):
        """Handle a basic math operation (add/subtract/multiply/divide).

        Two operands are popped from the stack, the mathematical operation is
        performed, and the result is pushed back onto the stack.

        args:
            tok (token):    The token read by the parser"""

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
        """Handle other mathematical operations.

        The required number of operands are popped from the stack, the
        mathematical operation is performed, and the result is pushed back
        onto the stack.

        args:
            tok (token):    The token read by the parser"""

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
        """Handle stack manipulation operations.

        The following operations are supported:

        +-----------+---------------------+----------------------+
        | Operation | Input Stack Diagram | Output Stack Diagram |
        +===========+=====================+======================+
        | DUP       | n                   | n n                  |
        +-----------+---------------------+----------------------+
        | SWAP      | x y                 | y x                  |
        +-----------+---------------------+----------------------+
        | ROLL      | a b c d             | d a b c              |
        +-----------+---------------------+----------------------+
        | ROLLD     | a b c d             | b c d a              |
        +-----------+---------------------+----------------------+
        | DEPTH     | a b c d             | a b c d 4            |
        +-----------+---------------------+----------------------+
        """

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
        """Handle a token from the input stream.

        This method is called once for each token from the input stream.
        If the token is a number, it's pushed onto the stack. If it's
        a mathematical operation, a call is made to ``check_arity`` and then
        the operation is performed. If the token is a stack operation, the
        operation is performed.

        args:
            tok (token):    The next token read from the input stream.

        returns:
            bool:   True if the token was handled, False otherwise."""

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
        """Tokenize a string of RPN and process it.

        args:
            input_line (str):       The RPN commands to process
            result_only (bool):     Select what to return from ``calculate()``

        returns:
            float:      The bottom element of the stack if ``result_only`` is True
            namedtuple: A named tuple containing both the result and the stack
                        if ``result_only`` is False."""

        for tok in self.lexer.tokenize(input_line):
            self.handle_token(tok)
        if result_only:
            return self.stack[-1]
        else:
            RpnCalcResult = namedtuple(RpnCalcResult, ['result', 'stack'])
            r = RpnCalcResult(result=self.stack[-1], stack=self.stack)
            return r
