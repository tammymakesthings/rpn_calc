# SPDX-FileCopyrightText: 2019-2023, Tammy Cravit
#
# SPDX-License-Identifier: MIT

from sly import Lexer

"""
.. module:: rpn_calc
    :synopsis: Simple RPN calculator with a sly-based parser.

    .. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""


class CalcLexer(Lexer):
    """Lexer for the rpn_calc calculator.

    The lexer is responsible for tokenizing the input to the calculator.
    Tokens are divided into one of the following categories:

    +----------+------------+--------------------------------+--------------+
    | Token(s) | Token Type | Description                    | Stack Arity  |
    +==========+============+================================+==============+
    | Numbers  | NUMBER     | Floating-point number format   | n/a          |
    +----------+------------+--------------------------------=--------------+
    | +        | PLUS       | Addition operation             | 2            |
    +----------+------------+--------------------------------+--------------+
    | -        | MINUS      | Subtraction operation          | 2            |
    +----------+------------+--------------------------------+--------------+
    | *        | TIMES      | Multiplication operation       | 2            |
    +----------+------------+--------------------------------+--------------+
    | /        | DIV        | Division operation             | 2            |
    +----------+------------+--------------------------------+--------------+
    | SIN      | ARITY1FUNC | Mathematical operations - 1    | 1            |
    | COS      |            | operand                        |              |
    | TAN      |            |                                |              |
    | SQRT     |            |                                |              |
    +----------+------------+--------------------------------+--------------+
    | EXP      | ARITY2FUNC | Mathematical operations - 2    | 2            |
    | NPR      |            | operands                       |              |
    | NCR      |            |                                |              |
    +----------+------------+--------------------------------+--------------+
    | DUP      | STACKOP    | Stack operations               | DUP - 1      |
    | SWAP     |            |                                | SWAP - 2     |
    | DROP     |            |                                | DROP - 1     |
    | ROLL     |            |                                | ROLL - 3+    |
    | ROLLD    |            |                                | ROLLD - 3+   |
    | DEPTH    |            |                                | DEPTH - 0    |
    +----------+------------+--------------------------------+--------------+
    | !STACK   | INLINE_CMD | Inline commands (only valid in | n/a          |
    | !VERSION |            | the REPL)                      |              |
    | !VERBOSE |            |                                |              |
    | !DEBUG   |            |                                |              |
    | !HELP    |            |                                |              |
    | !QUOT    |            |                                |              |
    +----------+------------+--------------------------------+--------------+

    Parsing is provided by the ``fly`` library. Spaces, tabs, and newline
    characters are ignored.
    """

    tokens = {
        ID,
        NUMBER,
        PLUS,
        MINUS,
        TIMES,
        DIV,
        ARITY1FUNC,
        ARITY2FUNC,
        STACKOP,
        INLINE_CMD,
    }
    """str: Classes of tokens recognized by the lexer"""

    ignore = " \t\n"
    """str: characters ignored by the lexer"""

    NUMBER = r"\-?\d+([\.]\d+)?"
    """str: regex to identify numbers"""

    ID = r"[a-zA-Z_!][a-zA-Z0-9_!]*"
    """str: regex to identity other tokens; they're subcategorized later"""

    ID["SIN"] = ARITY1FUNC
    ID["COS"] = ARITY1FUNC
    ID["TAN"] = ARITY1FUNC
    ID["SQRT"] = ARITY1FUNC

    ID["EXP"] = ARITY2FUNC
    ID["NCR"] = ARITY2FUNC
    ID["NPR"] = ARITY2FUNC

    ID["DUP"] = STACKOP
    ID["SWAP"] = STACKOP
    ID["DROP"] = STACKOP
    ID["ROLL"] = STACKOP
    ID["ROLLD"] = STACKOP
    ID["DEPTH"] = STACKOP

    ID["!STACK"] = INLINE_CMD
    ID["!VERSION"] = INLINE_CMD
    ID["!VERBOSE"] = INLINE_CMD
    ID["!DEBUG"] = INLINE_CMD
    ID["!QUIT"] = INLINE_CMD
    ID["!HELP"] = INLINE_CMD

    PLUS = r"\+"
    MINUS = r"\-"
    TIMES = r"\*"
    DIV = r"\/"

    def error(self, t):
        """Print an error message when an unrecognized token is encountered

        Args:
            t (str): The unrecognized token"""

        print("Line %d: Bad character %r" % (self.lineno, t.value[0]))
        self.index += 1
