from calc_lexer import CalcLexer
from calc_main import CalcMain
from calc_config import CalcConfig
from calc_version import *
import argparse

"""
.. module:: rpn_calc
    :synopsis: Simple RPN calculator with a sly-based parser.

    .. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""

class CalcRepl:
    """Provide an interactive interface to the calculator."""


    def __init__(self, Verbose=False, Debug=False):
        """Create an instance of the REPL class and read the configuration
        file if present.

        args:
            Verbose (bool): Print the stack contents after every operation.
                            Overrides the configuration file if ``Verbose`` is
                            true but the option is False in the configuration file.
            Debug (bool):   Print debugging output during parsing. Overrides the
                            configuration file if ``Debug`` is true but the
                            option is False in the configuration file."""

        self.read_config()

        if Verbose is True:
            self.verbose = True
        if Debug is True:
            self.debug = True

        self.calc = CalcMain()


    def read_config(self):
        """Read the configurtion file if present, or supply default values
        if it's not present."""

        config_parser = CalcConfig()
        if config_parser.config_values['debug']:
            if config_parser.did_use_defaults:
                print("* DEBUG: Used default config file values")
            else:
                print(f"* DEBUG: Read config file: {config_parser.config_file}")

        self.verbose = config_parser.config_values['verbose']
        self.debug = config_parser.config_values['debug']


    def print_version(self):
        """Print the calculator version number and the settings of the Debug
        and Verbose flags."""

        print(f"Version {RPN_CALC_VERSION}, Debug={self.debug}, Verbose={self.verbose}")


    def print_banner(self):
        """Print the REPL startup banner"""

        print("****************************************************************************")
        print("*              rpn_calc: Simple RPN calculator with Sly lexer              *")
        print("*                 Tammy Cravit, tammymakesthings@gmail.com                 *")
        print("****************************************************************************")
        print("")
        self.print_version()
        print("Type !HELP for help.")
        print("")


    def do_help(self):
        """Print a help message in response to the !HELP command."""

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
        """Exit the REPL in response to the !QUIT command."""

        print("Exiting.")
        exit(0)


    def print_stack(self, all_levels=False, prefix=""):
        """Print the contents of the stack in response to the !STACK command.

        args:
            all_levels (bool):  True to print the whole stack, False to just
                                print the bottom stack element.
            prefix (str):       If not empty, each line of the output will be
                                preceded by this text."""
        if all_levels:
            print(f"{prefix}[{self.calc.stack_depth()}] {self.calc.stack_repr()}\n")
        else:
            if self.calc.stack_depth() > 0:
                print(f"{prefix}[{self.calc.stack_depth()}] {self.calc.stack[-1]}\n")
            else:
                print(f"{prefix}[0]\n")

    def handle_inline_cmd(self, tok):
        """Handle REPL commands.

        The following commands are supported:

        +----------+--------------------------------------+
        | Command  | Description                          |
        +==========+======================================+
        | !STACK   | Print the contents of the stack      |
        +----------+--------------------------------------+
        | !VERBOSE | Toggle the verbose output flag       |
        +----------+--------------------------------------+
        | !DEBUG   | Toggle the printihng of debug output |
        +----------+--------------------------------------+
        | !VERSION | Print the calculator version string  |
        +----------+--------------------------------------+
        | !HELP    | Print the calculator help message    |
        +----------+--------------------------------------+
        | !QUIT    | Exit the REPL                        |
        +----------+--------------------------------------+
        """

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
        """Run the calculator REPL."""

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


    @staticmethod
    def shell():
        """Run the REPL from the command line."""

        parser = argparse.ArgumentParser(description='Simple RPN Calculator.')
        parser.add_argument('-v', '--verbose', help='Print the full stack after each calculation.', action='store_true')
        parser.add_argument('-d', '--debug', help='Print additional debugging output.', action='store_true')
        args = parser.parse_args()
        print(args)
        repl = CalcRepl(Verbose = args.verbose, Debug = args.debug)
        repl.repl()


if __name__ == "__main__":
    CalcRepl.shell()
