from calc_lexer import CalcLexer
from calc_main import CalcMain
from calc_config import CalcConfig
from calc_version import *

class CalcRepl:

    def __init__(self, Verbose=False, Debug=False):
        self.verbose = Verbose
        self.debug = Debug
        self.read_config()
        self.calc = CalcMain()
        self.repl()

    def read_config(self):
        config_parser = CalcConfig()
        if config_parser.config_values['debug']:
            if config_parser.did_use_defaults:
                print("* DEBUG: Used default config file values")
            else:
                print(f"* DEBUG: Read config file: {config_parser.config_file}")

        self.verbose = config_parser.config_values['verbose']
        self.debug = config_parser.config_values['debug']

    def print_version(self):
        print(f"Version {RPN_CALC_VERSION}, Debug={self.debug}, Verbose={self.verbose}")

    def print_banner(self):
        print("****************************************************************************")
        print("*              rpn_calc: Simple RPN calculator with Sly lexer              *")
        print("*                 Tammy Cravit, tammymakesthings@gmail.com                 *")
        print("****************************************************************************")
        print("")
        self.print_version()
        print("Type !HELP for help.")
        print("")

    def do_help(self):
        print("rpn_calc help:")
        print("   - Input is in RPN format (see https://en.wikipedia.org/wiki/Reverse_Polish_notation)")
        print("   - Whitespace is ignored")
        print("   - Input is parsed on end of line")
        print("")
        print("Math operators (arity=2): + - * / EXP NCR NPR")
        print("Math operators (arity=1): SIN COS TAN SQRT LOG LN")
        print("Stack operators         : DUP DROP SWAP ROLL ROLLD DEPTH")
        print("")
        print ("Inline commands:")
        print("   !STACK   - print contents of stack")
        print("   !VERBOSE - print full stack after every op instead of bottom element")
        print("   !DEBUG   - print debugging information during parsing")
        print("   !HELP    - print this help message")
        print("   !QUIT    - exit the program")
        print("")

    def do_exit(self):
        print("Exiting.")
        exit(0)

    def print_stack(self, all_levels=False, prefix=""):
        if all_levels:
            print(f"{prefix}[{self.calc.stack_depth()}] {self.calc.stack_repr()}\n")
        else:
            print(f"{prefix}[{self.calc.stack_depth()}] {self.calc.stack[-1]}\n")

    def handle_inline_cmd(self, tok):
        if tok.value   == "!STACK":
            self.print_stack(all_levels=True, prefix="STACK: ")
        elif tok.value == "!VERSION":
            self.print_version()
        elif tok.value == "!VERBOSE":
            if self.calc.verbose:
                print("* Stack printing after each operation DISABLED")
                self.calc.verbose = False
            else:
                print("* Stack printing after each operation ENABLED")
                self.calc.verbose = True
        elif tok.value == "!DEBUG":
            if self.calc.debug:
                print("* Debug printing DISABLED")
                self.calc.debug = False
            else:
                print("* Debug printing  ENABLED")
                self.calc.debug = True
        elif tok.value == "!HELP":
            self.do_help()

        elif tok.value == "!QUIT":
            self.do_exit()


    def repl(self):
        self.print_banner()

        while True:
            was_inline_cmd = False
            try:
                input_line = input('calc> ').upper()
                for tok in self.calc.lexer.tokenize(input_line):
                    if self.calc.handle_token(tok) == False:
                        if self.handle_inline_cmd(tok) == False:
                            print(f"* Unhandled token: {tok}")
                        else:
                            was_inline_cmd = True

                    if self.debug:
                        print(f"* DEBUG: Tok was {tok}, stack is now {self.stack_repr()}")
                if was_inline_cmd == False:
                    if self.verbose:
                        self.print_stack(all_levels=True)
                    else:
                        self.print_stack()

            except EOFError:
                self.do_exit()
        self.do_exit()

if __name__ == "__main__":
    repl = CalcRepl()
    repl.repl()