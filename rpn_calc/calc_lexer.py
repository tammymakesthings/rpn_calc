from sly import Lexer

class CalcLexer(Lexer):
    tokens = {
        ID,
        NUMBER,
        PLUS, MINUS, TIMES, DIV,
        ARITY1FUNC, ARITY2FUNC, STACKOP, INLINE_CMD
    }
    ignore = ' \t\n'

    NUMBER = r'\-?\d+([\.]\d+)?'
    ID     = r'[a-zA-Z_!][a-zA-Z0-9_!]*'

    ID['SIN']      = ARITY1FUNC
    ID['COS']      = ARITY1FUNC
    ID['TAN']      = ARITY1FUNC
    ID['SQRT']     = ARITY1FUNC

    ID['EXP']      = ARITY2FUNC
    ID['NCR']      = ARITY2FUNC
    ID['NPR']      = ARITY2FUNC

    ID['DUP']      = STACKOP
    ID['SWAP']     = STACKOP
    ID['DROP']     = STACKOP
    ID['ROLL']     = STACKOP
    ID['ROLLD']    = STACKOP
    ID['DEPTH']    = STACKOP

    ID['!STACK']   = INLINE_CMD
    ID['!VERSION'] = INLINE_CMD
    ID['!VERBOSE'] = INLINE_CMD
    ID['!DEBUG']   = INLINE_CMD
    ID['!QUIT']    = INLINE_CMD
    ID['!HELP']    = INLINE_CMD

    PLUS           = r'\+'
    MINUS          = r'\-'
    TIMES          = r'\*'
    DIV            = r'\/'

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__=='__main__':
    test = '''
    1.2345 -2454 22 + 3 - 4 * 5 / 1 COS 2 SIN 3 TAN 4
    1 DUP 1 2 3 SWAP DROP ROLL ROLLD 13
    SQRT 1 2 EXP 49 6 NCR 49 6 NPR DEPTH
    !STACK !VERSION !QUIT
    '''.upper()
    lexer = CalcLexer()
    for tok in lexer.tokenize(test):
        print(tok)
