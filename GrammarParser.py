# Generated from Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,339,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,4,0,76,8,0,11,0,12,0,77,1,
        0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,125,8,8,10,
        8,12,8,128,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,138,8,9,10,9,
        12,9,141,9,9,1,9,1,9,1,10,1,10,3,10,147,8,10,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,155,8,11,1,12,1,12,1,12,1,12,3,12,161,8,12,1,13,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,24,5,24,220,8,24,10,24,12,24,223,9,24,1,24,3,24,226,
        8,24,1,25,1,25,1,25,1,25,3,25,232,8,25,1,26,1,26,1,27,1,27,1,27,
        1,27,3,27,240,8,27,1,28,1,28,1,28,1,28,1,28,1,28,3,28,248,8,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,3,31,294,8,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,
        34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,0,
        0,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,1,1,0,7,12,324,0,
        75,1,0,0,0,2,81,1,0,0,0,4,85,1,0,0,0,6,89,1,0,0,0,8,94,1,0,0,0,10,
        99,1,0,0,0,12,104,1,0,0,0,14,111,1,0,0,0,16,118,1,0,0,0,18,131,1,
        0,0,0,20,146,1,0,0,0,22,154,1,0,0,0,24,160,1,0,0,0,26,162,1,0,0,
        0,28,167,1,0,0,0,30,172,1,0,0,0,32,177,1,0,0,0,34,182,1,0,0,0,36,
        187,1,0,0,0,38,192,1,0,0,0,40,197,1,0,0,0,42,202,1,0,0,0,44,207,
        1,0,0,0,46,210,1,0,0,0,48,225,1,0,0,0,50,231,1,0,0,0,52,233,1,0,
        0,0,54,239,1,0,0,0,56,247,1,0,0,0,58,251,1,0,0,0,60,257,1,0,0,0,
        62,293,1,0,0,0,64,295,1,0,0,0,66,303,1,0,0,0,68,325,1,0,0,0,70,330,
        1,0,0,0,72,336,1,0,0,0,74,76,3,54,27,0,75,74,1,0,0,0,76,77,1,0,0,
        0,77,75,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,0,0,1,80,1,1,
        0,0,0,81,82,3,18,9,0,82,83,5,3,0,0,83,84,3,18,9,0,84,3,1,0,0,0,85,
        86,3,16,8,0,86,87,5,3,0,0,87,88,3,16,8,0,88,5,1,0,0,0,89,90,5,20,
        0,0,90,91,5,30,0,0,91,92,3,24,12,0,92,93,5,31,0,0,93,7,1,0,0,0,94,
        95,5,21,0,0,95,96,5,30,0,0,96,97,3,24,12,0,97,98,5,31,0,0,98,9,1,
        0,0,0,99,100,5,23,0,0,100,101,5,30,0,0,101,102,3,24,12,0,102,103,
        5,31,0,0,103,11,1,0,0,0,104,105,5,24,0,0,105,106,5,30,0,0,106,107,
        3,24,12,0,107,108,5,15,0,0,108,109,5,43,0,0,109,110,5,31,0,0,110,
        13,1,0,0,0,111,112,5,22,0,0,112,113,5,30,0,0,113,114,3,24,12,0,114,
        115,5,15,0,0,115,116,5,43,0,0,116,117,5,31,0,0,117,15,1,0,0,0,118,
        119,5,34,0,0,119,120,5,43,0,0,120,126,5,44,0,0,121,122,5,15,0,0,
        122,123,5,44,0,0,123,125,5,43,0,0,124,121,1,0,0,0,125,128,1,0,0,
        0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,126,1,0,0,
        0,129,130,5,35,0,0,130,17,1,0,0,0,131,132,5,34,0,0,132,133,3,16,
        8,0,133,139,5,44,0,0,134,135,5,15,0,0,135,136,5,44,0,0,136,138,3,
        16,8,0,137,134,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,
        0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,5,35,0,0,143,19,1,
        0,0,0,144,147,3,6,3,0,145,147,3,8,4,0,146,144,1,0,0,0,146,145,1,
        0,0,0,147,21,1,0,0,0,148,155,3,20,10,0,149,155,3,6,3,0,150,155,3,
        8,4,0,151,155,3,10,5,0,152,155,3,12,6,0,153,155,3,14,7,0,154,148,
        1,0,0,0,154,149,1,0,0,0,154,150,1,0,0,0,154,151,1,0,0,0,154,152,
        1,0,0,0,154,153,1,0,0,0,155,23,1,0,0,0,156,161,3,22,11,0,157,161,
        3,18,9,0,158,161,3,16,8,0,159,161,5,43,0,0,160,156,1,0,0,0,160,157,
        1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,25,1,0,0,0,162,163,5,
        16,0,0,163,164,5,30,0,0,164,165,3,24,12,0,165,166,5,31,0,0,166,27,
        1,0,0,0,167,168,5,17,0,0,168,169,5,30,0,0,169,170,3,24,12,0,170,
        171,5,31,0,0,171,29,1,0,0,0,172,173,5,18,0,0,173,174,5,30,0,0,174,
        175,3,24,12,0,175,176,5,31,0,0,176,31,1,0,0,0,177,178,5,19,0,0,178,
        179,5,30,0,0,179,180,3,24,12,0,180,181,5,31,0,0,181,33,1,0,0,0,182,
        183,5,27,0,0,183,184,5,30,0,0,184,185,3,24,12,0,185,186,5,31,0,0,
        186,35,1,0,0,0,187,188,5,28,0,0,188,189,5,30,0,0,189,190,3,24,12,
        0,190,191,5,31,0,0,191,37,1,0,0,0,192,193,5,29,0,0,193,194,5,30,
        0,0,194,195,3,24,12,0,195,196,5,31,0,0,196,39,1,0,0,0,197,198,5,
        25,0,0,198,199,5,30,0,0,199,200,3,24,12,0,200,201,5,31,0,0,201,41,
        1,0,0,0,202,203,5,26,0,0,203,204,5,30,0,0,204,205,3,24,12,0,205,
        206,5,31,0,0,206,43,1,0,0,0,207,208,3,24,12,0,208,209,5,14,0,0,209,
        45,1,0,0,0,210,211,3,24,12,0,211,212,5,5,0,0,212,213,3,24,12,0,213,
        47,1,0,0,0,214,215,3,50,25,0,215,221,5,44,0,0,216,217,5,15,0,0,217,
        218,5,44,0,0,218,220,3,50,25,0,219,216,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,221,222,1,0,0,0,222,226,1,0,0,0,223,221,1,0,0,0,224,
        226,3,52,26,0,225,214,1,0,0,0,225,224,1,0,0,0,226,49,1,0,0,0,227,
        232,5,37,0,0,228,229,5,37,0,0,229,230,5,13,0,0,230,232,3,24,12,0,
        231,227,1,0,0,0,231,228,1,0,0,0,232,51,1,0,0,0,233,234,1,0,0,0,234,
        53,1,0,0,0,235,240,3,56,28,0,236,237,3,56,28,0,237,238,3,54,27,0,
        238,240,1,0,0,0,239,235,1,0,0,0,239,236,1,0,0,0,240,55,1,0,0,0,241,
        248,3,58,29,0,242,248,3,24,12,0,243,248,3,62,31,0,244,248,3,66,33,
        0,245,248,3,68,34,0,246,248,3,60,30,0,247,241,1,0,0,0,247,242,1,
        0,0,0,247,243,1,0,0,0,247,244,1,0,0,0,247,245,1,0,0,0,247,246,1,
        0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,250,5,45,0,0,250,57,1,
        0,0,0,251,252,5,37,0,0,252,253,5,44,0,0,253,254,5,13,0,0,254,255,
        5,44,0,0,255,256,3,24,12,0,256,59,1,0,0,0,257,258,5,38,0,0,258,259,
        5,44,0,0,259,260,5,30,0,0,260,261,5,44,0,0,261,262,3,48,24,0,262,
        263,5,44,0,0,263,264,5,31,0,0,264,265,5,44,0,0,265,266,5,32,0,0,
        266,267,5,44,0,0,267,268,3,54,27,0,268,269,5,44,0,0,269,270,5,33,
        0,0,270,61,1,0,0,0,271,272,5,39,0,0,272,273,5,44,0,0,273,274,3,70,
        35,0,274,275,5,44,0,0,275,276,5,32,0,0,276,277,5,44,0,0,277,278,
        3,54,27,0,278,279,5,44,0,0,279,280,5,33,0,0,280,294,1,0,0,0,281,
        282,5,39,0,0,282,283,5,44,0,0,283,284,3,70,35,0,284,285,5,44,0,0,
        285,286,5,32,0,0,286,287,5,44,0,0,287,288,3,54,27,0,288,289,5,44,
        0,0,289,290,5,33,0,0,290,291,5,44,0,0,291,292,3,64,32,0,292,294,
        1,0,0,0,293,271,1,0,0,0,293,281,1,0,0,0,294,63,1,0,0,0,295,296,5,
        40,0,0,296,297,5,44,0,0,297,298,5,32,0,0,298,299,5,44,0,0,299,300,
        3,54,27,0,300,301,5,44,0,0,301,302,5,33,0,0,302,65,1,0,0,0,303,304,
        5,42,0,0,304,305,5,44,0,0,305,306,5,37,0,0,306,307,5,44,0,0,307,
        308,5,13,0,0,308,309,5,44,0,0,309,310,3,24,12,0,310,311,5,44,0,0,
        311,312,5,36,0,0,312,313,5,44,0,0,313,314,3,24,12,0,314,315,5,44,
        0,0,315,316,5,36,0,0,316,317,5,44,0,0,317,318,3,24,12,0,318,319,
        5,44,0,0,319,320,5,32,0,0,320,321,5,44,0,0,321,322,3,54,27,0,322,
        323,5,44,0,0,323,324,5,33,0,0,324,67,1,0,0,0,325,326,5,41,0,0,326,
        327,5,30,0,0,327,328,3,24,12,0,328,329,5,31,0,0,329,69,1,0,0,0,330,
        331,3,24,12,0,331,332,5,44,0,0,332,333,3,72,36,0,333,334,5,44,0,
        0,334,335,3,24,12,0,335,71,1,0,0,0,336,337,7,0,0,0,337,73,1,0,0,
        0,12,77,126,139,146,154,160,221,225,231,239,247,293
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'='", "'<>'", "'<'", "'>'", "'<='", "'>='", "':='", 
                     "'!'", "','", "'exp'", "'abs'", "'ceil'", "'floor'", 
                     "'sin'", "'cos'", "'log'", "'sqrt'", "'root'", "'sinh'", 
                     "'cosh'", "'arcsin'", "'arccos'", "'arctan'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "<INVALID>", 
                     "'func'", "'if'", "'else'", "'print'", "'for'", "<INVALID>", 
                     "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", 
                      "MOD", "POWER", "EQUALS", "NOT_EQUALS", "LESS_THAN", 
                      "GREATER_THAN", "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", 
                      "ASSIGNMENT", "FACTORIAL", "COMMA", "EXP", "ABS", 
                      "CEIL", "FLOOR", "SIN", "COS", "LOG", "SQRT", "ROOT", 
                      "SINH", "COSH", "ARCSIN", "ARCCOS", "ARCTAN", "PAR_LEFT", 
                      "PAR_RIGHT", "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT", 
                      "BRACKET_RIGHT", "SEMICOLON", "VARIABLE", "FUNC", 
                      "IF", "ELSE", "PRINT", "FOR", "NUMBER", "SPACE", "NEWLINE" ]

    RULE_program = 0
    RULE_matmul = 1
    RULE_dot_product = 2
    RULE_sin = 3
    RULE_cos = 4
    RULE_sqrt = 5
    RULE_root = 6
    RULE_log = 7
    RULE_vector = 8
    RULE_matrix = 9
    RULE_trig_func = 10
    RULE_built_in_func = 11
    RULE_expression = 12
    RULE_exp_func = 13
    RULE_abs_func = 14
    RULE_ceil_func = 15
    RULE_floor_func = 16
    RULE_arcsin_func = 17
    RULE_arccos_func = 18
    RULE_arctan_func = 19
    RULE_sinh_func = 20
    RULE_cosh_func = 21
    RULE_factorial_func = 22
    RULE_modulo_op = 23
    RULE_params = 24
    RULE_param = 25
    RULE_empty = 26
    RULE_statements = 27
    RULE_statement = 28
    RULE_assignment_statement = 29
    RULE_func_statement = 30
    RULE_if_statement = 31
    RULE_else_statement = 32
    RULE_for_statement = 33
    RULE_print_statement = 34
    RULE_condition = 35
    RULE_logic_op = 36

    ruleNames =  [ "program", "matmul", "dot_product", "sin", "cos", "sqrt", 
                   "root", "log", "vector", "matrix", "trig_func", "built_in_func", 
                   "expression", "exp_func", "abs_func", "ceil_func", "floor_func", 
                   "arcsin_func", "arccos_func", "arctan_func", "sinh_func", 
                   "cosh_func", "factorial_func", "modulo_op", "params", 
                   "param", "empty", "statements", "statement", "assignment_statement", 
                   "func_statement", "if_statement", "else_statement", "for_statement", 
                   "print_statement", "condition", "logic_op" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MULTIPLICATION=3
    DIVISION=4
    MOD=5
    POWER=6
    EQUALS=7
    NOT_EQUALS=8
    LESS_THAN=9
    GREATER_THAN=10
    LESS_THAN_EQUALS=11
    GREATER_THAN_EQUALS=12
    ASSIGNMENT=13
    FACTORIAL=14
    COMMA=15
    EXP=16
    ABS=17
    CEIL=18
    FLOOR=19
    SIN=20
    COS=21
    LOG=22
    SQRT=23
    ROOT=24
    SINH=25
    COSH=26
    ARCSIN=27
    ARCCOS=28
    ARCTAN=29
    PAR_LEFT=30
    PAR_RIGHT=31
    BRACE_LEFT=32
    BRACE_RIGHT=33
    BRACKET_LEFT=34
    BRACKET_RIGHT=35
    SEMICOLON=36
    VARIABLE=37
    FUNC=38
    IF=39
    ELSE=40
    PRINT=41
    FOR=42
    NUMBER=43
    SPACE=44
    NEWLINE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementsContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementsContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.statements()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 51556819927040) != 0)):
                    break

            self.state = 79
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.MatrixContext)
            else:
                return self.getTypedRuleContext(GrammarParser.MatrixContext,i)


        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_matmul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatmul" ):
                listener.enterMatmul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatmul" ):
                listener.exitMatmul(self)




    def matmul(self):

        localctx = GrammarParser.MatmulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_matmul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.matrix()
            self.state = 82
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 83
            self.matrix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VectorContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VectorContext,i)


        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_dot_product

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_product" ):
                listener.enterDot_product(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_product" ):
                listener.exitDot_product(self)




    def dot_product(self):

        localctx = GrammarParser.Dot_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dot_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.vector()
            self.state = 86
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 87
            self.vector()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(GrammarParser.SIN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)




    def sin(self):

        localctx = GrammarParser.SinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(GrammarParser.SIN)
            self.state = 90
            self.match(GrammarParser.PAR_LEFT)
            self.state = 91
            self.expression()
            self.state = 92
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(GrammarParser.COS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_cos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)




    def cos(self):

        localctx = GrammarParser.CosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GrammarParser.COS)
            self.state = 95
            self.match(GrammarParser.PAR_LEFT)
            self.state = 96
            self.expression()
            self.state = 97
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqrtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQRT(self):
            return self.getToken(GrammarParser.SQRT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sqrt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrt" ):
                listener.enterSqrt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrt" ):
                listener.exitSqrt(self)




    def sqrt(self):

        localctx = GrammarParser.SqrtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sqrt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(GrammarParser.SQRT)
            self.state = 100
            self.match(GrammarParser.PAR_LEFT)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT(self):
            return self.getToken(GrammarParser.ROOT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = GrammarParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GrammarParser.ROOT)
            self.state = 105
            self.match(GrammarParser.PAR_LEFT)
            self.state = 106
            self.expression()
            self.state = 107
            self.match(GrammarParser.COMMA)
            self.state = 108
            self.match(GrammarParser.NUMBER)
            self.state = 109
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(GrammarParser.LOG, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)




    def log(self):

        localctx = GrammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(GrammarParser.LOG)
            self.state = 112
            self.match(GrammarParser.PAR_LEFT)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(GrammarParser.COMMA)
            self.state = 115
            self.match(GrammarParser.NUMBER)
            self.state = 116
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(GrammarParser.BRACKET_LEFT, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NUMBER)
            else:
                return self.getToken(GrammarParser.NUMBER, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def BRACKET_RIGHT(self):
            return self.getToken(GrammarParser.BRACKET_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)




    def vector(self):

        localctx = GrammarParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(GrammarParser.BRACKET_LEFT)
            self.state = 119
            self.match(GrammarParser.NUMBER)
            self.state = 120
            self.match(GrammarParser.SPACE)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 121
                self.match(GrammarParser.COMMA)
                self.state = 122
                self.match(GrammarParser.SPACE)
                self.state = 123
                self.match(GrammarParser.NUMBER)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(GrammarParser.BRACKET_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(GrammarParser.BRACKET_LEFT, 0)

        def vector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VectorContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VectorContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def BRACKET_RIGHT(self):
            return self.getToken(GrammarParser.BRACKET_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)




    def matrix(self):

        localctx = GrammarParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(GrammarParser.BRACKET_LEFT)
            self.state = 132
            self.vector()
            self.state = 133
            self.match(GrammarParser.SPACE)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 134
                self.match(GrammarParser.COMMA)
                self.state = 135
                self.match(GrammarParser.SPACE)
                self.state = 136
                self.vector()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(GrammarParser.BRACKET_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trig_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sin(self):
            return self.getTypedRuleContext(GrammarParser.SinContext,0)


        def cos(self):
            return self.getTypedRuleContext(GrammarParser.CosContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_trig_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrig_func" ):
                listener.enterTrig_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrig_func" ):
                listener.exitTrig_func(self)




    def trig_func(self):

        localctx = GrammarParser.Trig_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_trig_func)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.sin()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.cos()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Built_in_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trig_func(self):
            return self.getTypedRuleContext(GrammarParser.Trig_funcContext,0)


        def sin(self):
            return self.getTypedRuleContext(GrammarParser.SinContext,0)


        def cos(self):
            return self.getTypedRuleContext(GrammarParser.CosContext,0)


        def sqrt(self):
            return self.getTypedRuleContext(GrammarParser.SqrtContext,0)


        def root(self):
            return self.getTypedRuleContext(GrammarParser.RootContext,0)


        def log(self):
            return self.getTypedRuleContext(GrammarParser.LogContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_built_in_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilt_in_func" ):
                listener.enterBuilt_in_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilt_in_func" ):
                listener.exitBuilt_in_func(self)




    def built_in_func(self):

        localctx = GrammarParser.Built_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_built_in_func)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.trig_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.sin()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.cos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.sqrt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.root()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 153
                self.log()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def built_in_func(self):
            return self.getTypedRuleContext(GrammarParser.Built_in_funcContext,0)


        def matrix(self):
            return self.getTypedRuleContext(GrammarParser.MatrixContext,0)


        def vector(self):
            return self.getTypedRuleContext(GrammarParser.VectorContext,0)


        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.built_in_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.matrix()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.vector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.match(GrammarParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP(self):
            return self.getToken(GrammarParser.EXP, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_exp_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_func" ):
                listener.enterExp_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_func" ):
                listener.exitExp_func(self)




    def exp_func(self):

        localctx = GrammarParser.Exp_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GrammarParser.EXP)
            self.state = 163
            self.match(GrammarParser.PAR_LEFT)
            self.state = 164
            self.expression()
            self.state = 165
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABS(self):
            return self.getToken(GrammarParser.ABS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_abs_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs_func" ):
                listener.enterAbs_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs_func" ):
                listener.exitAbs_func(self)




    def abs_func(self):

        localctx = GrammarParser.Abs_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_abs_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(GrammarParser.ABS)
            self.state = 168
            self.match(GrammarParser.PAR_LEFT)
            self.state = 169
            self.expression()
            self.state = 170
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ceil_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CEIL(self):
            return self.getToken(GrammarParser.CEIL, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_ceil_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeil_func" ):
                listener.enterCeil_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeil_func" ):
                listener.exitCeil_func(self)




    def ceil_func(self):

        localctx = GrammarParser.Ceil_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ceil_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(GrammarParser.CEIL)
            self.state = 173
            self.match(GrammarParser.PAR_LEFT)
            self.state = 174
            self.expression()
            self.state = 175
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floor_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOOR(self):
            return self.getToken(GrammarParser.FLOOR, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_floor_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_func" ):
                listener.enterFloor_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_func" ):
                listener.exitFloor_func(self)




    def floor_func(self):

        localctx = GrammarParser.Floor_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_floor_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(GrammarParser.FLOOR)
            self.state = 178
            self.match(GrammarParser.PAR_LEFT)
            self.state = 179
            self.expression()
            self.state = 180
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arcsin_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCSIN(self):
            return self.getToken(GrammarParser.ARCSIN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arcsin_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArcsin_func" ):
                listener.enterArcsin_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArcsin_func" ):
                listener.exitArcsin_func(self)




    def arcsin_func(self):

        localctx = GrammarParser.Arcsin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arcsin_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(GrammarParser.ARCSIN)
            self.state = 183
            self.match(GrammarParser.PAR_LEFT)
            self.state = 184
            self.expression()
            self.state = 185
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arccos_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCCOS(self):
            return self.getToken(GrammarParser.ARCCOS, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arccos_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArccos_func" ):
                listener.enterArccos_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArccos_func" ):
                listener.exitArccos_func(self)




    def arccos_func(self):

        localctx = GrammarParser.Arccos_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arccos_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(GrammarParser.ARCCOS)
            self.state = 188
            self.match(GrammarParser.PAR_LEFT)
            self.state = 189
            self.expression()
            self.state = 190
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arctan_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARCTAN(self):
            return self.getToken(GrammarParser.ARCTAN, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arctan_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArctan_func" ):
                listener.enterArctan_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArctan_func" ):
                listener.exitArctan_func(self)




    def arctan_func(self):

        localctx = GrammarParser.Arctan_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arctan_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(GrammarParser.ARCTAN)
            self.state = 193
            self.match(GrammarParser.PAR_LEFT)
            self.state = 194
            self.expression()
            self.state = 195
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sinh_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINH(self):
            return self.getToken(GrammarParser.SINH, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_sinh_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinh_func" ):
                listener.enterSinh_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinh_func" ):
                listener.exitSinh_func(self)




    def sinh_func(self):

        localctx = GrammarParser.Sinh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sinh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(GrammarParser.SINH)
            self.state = 198
            self.match(GrammarParser.PAR_LEFT)
            self.state = 199
            self.expression()
            self.state = 200
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cosh_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COSH(self):
            return self.getToken(GrammarParser.COSH, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_cosh_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosh_func" ):
                listener.enterCosh_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosh_func" ):
                listener.exitCosh_func(self)




    def cosh_func(self):

        localctx = GrammarParser.Cosh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cosh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(GrammarParser.COSH)
            self.state = 203
            self.match(GrammarParser.PAR_LEFT)
            self.state = 204
            self.expression()
            self.state = 205
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factorial_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def FACTORIAL(self):
            return self.getToken(GrammarParser.FACTORIAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_factorial_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorial_func" ):
                listener.enterFactorial_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorial_func" ):
                listener.exitFactorial_func(self)




    def factorial_func(self):

        localctx = GrammarParser.Factorial_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_factorial_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expression()
            self.state = 208
            self.match(GrammarParser.FACTORIAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Modulo_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_modulo_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo_op" ):
                listener.enterModulo_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo_op" ):
                listener.exitModulo_op(self)




    def modulo_op(self):

        localctx = GrammarParser.Modulo_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_modulo_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expression()
            self.state = 211
            self.match(GrammarParser.MOD)
            self.state = 212
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ParamContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ParamContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def empty(self):
            return self.getTypedRuleContext(GrammarParser.EmptyContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = GrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.param()
                self.state = 215
                self.match(GrammarParser.SPACE)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 216
                    self.match(GrammarParser.COMMA)
                    self.state = 217
                    self.match(GrammarParser.SPACE)
                    self.state = 218
                    self.param()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.empty()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = GrammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(GrammarParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(GrammarParser.VARIABLE)
                self.state = 229
                self.match(GrammarParser.ASSIGNMENT)
                self.state = 230
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)




    def empty(self):

        localctx = GrammarParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_empty)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = GrammarParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statements)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.statement()
                self.state = 237
                self.statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(GrammarParser.NEWLINE, 0)

        def assignment_statement(self):
            return self.getTypedRuleContext(GrammarParser.Assignment_statementContext,0)


        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(GrammarParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(GrammarParser.For_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(GrammarParser.Print_statementContext,0)


        def func_statement(self):
            return self.getTypedRuleContext(GrammarParser.Func_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.state = 241
                self.assignment_statement()
                pass
            elif token in [20, 21, 22, 23, 24, 34, 43]:
                self.state = 242
                self.expression()
                pass
            elif token in [39]:
                self.state = 243
                self.if_statement()
                pass
            elif token in [42]:
                self.state = 244
                self.for_statement()
                pass
            elif token in [41]:
                self.state = 245
                self.print_statement()
                pass
            elif token in [38]:
                self.state = 246
                self.func_statement()
                pass
            elif token in [45]:
                pass
            else:
                pass
            self.state = 249
            self.match(GrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




    def assignment_statement(self):

        localctx = GrammarParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(GrammarParser.VARIABLE)
            self.state = 252
            self.match(GrammarParser.SPACE)
            self.state = 253
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 254
            self.match(GrammarParser.SPACE)
            self.state = 255
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GrammarParser.FUNC, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def params(self):
            return self.getTypedRuleContext(GrammarParser.ParamsContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_func_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_statement" ):
                listener.enterFunc_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_statement" ):
                listener.exitFunc_statement(self)




    def func_statement(self):

        localctx = GrammarParser.Func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(GrammarParser.FUNC)
            self.state = 258
            self.match(GrammarParser.SPACE)
            self.state = 259
            self.match(GrammarParser.PAR_LEFT)
            self.state = 260
            self.match(GrammarParser.SPACE)
            self.state = 261
            self.params()
            self.state = 262
            self.match(GrammarParser.SPACE)
            self.state = 263
            self.match(GrammarParser.PAR_RIGHT)
            self.state = 264
            self.match(GrammarParser.SPACE)
            self.state = 265
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 266
            self.match(GrammarParser.SPACE)
            self.state = 267
            self.statements()
            self.state = 268
            self.match(GrammarParser.SPACE)
            self.state = 269
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GrammarParser.IF, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def condition(self):
            return self.getTypedRuleContext(GrammarParser.ConditionContext,0)


        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def else_statement(self):
            return self.getTypedRuleContext(GrammarParser.Else_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = GrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_statement)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(GrammarParser.IF)
                self.state = 272
                self.match(GrammarParser.SPACE)
                self.state = 273
                self.condition()
                self.state = 274
                self.match(GrammarParser.SPACE)
                self.state = 275
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 276
                self.match(GrammarParser.SPACE)
                self.state = 277
                self.statements()
                self.state = 278
                self.match(GrammarParser.SPACE)
                self.state = 279
                self.match(GrammarParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(GrammarParser.IF)
                self.state = 282
                self.match(GrammarParser.SPACE)
                self.state = 283
                self.condition()
                self.state = 284
                self.match(GrammarParser.SPACE)
                self.state = 285
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 286
                self.match(GrammarParser.SPACE)
                self.state = 287
                self.statements()
                self.state = 288
                self.match(GrammarParser.SPACE)
                self.state = 289
                self.match(GrammarParser.BRACE_RIGHT)
                self.state = 290
                self.match(GrammarParser.SPACE)
                self.state = 291
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GrammarParser.ELSE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = GrammarParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(GrammarParser.ELSE)
            self.state = 296
            self.match(GrammarParser.SPACE)
            self.state = 297
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 298
            self.match(GrammarParser.SPACE)
            self.state = 299
            self.statements()
            self.state = 300
            self.match(GrammarParser.SPACE)
            self.state = 301
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def VARIABLE(self):
            return self.getToken(GrammarParser.VARIABLE, 0)

        def ASSIGNMENT(self):
            return self.getToken(GrammarParser.ASSIGNMENT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = GrammarParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(GrammarParser.FOR)
            self.state = 304
            self.match(GrammarParser.SPACE)
            self.state = 305
            self.match(GrammarParser.VARIABLE)
            self.state = 306
            self.match(GrammarParser.SPACE)
            self.state = 307
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 308
            self.match(GrammarParser.SPACE)
            self.state = 309
            self.expression()
            self.state = 310
            self.match(GrammarParser.SPACE)
            self.state = 311
            self.match(GrammarParser.SEMICOLON)
            self.state = 312
            self.match(GrammarParser.SPACE)
            self.state = 313
            self.expression()
            self.state = 314
            self.match(GrammarParser.SPACE)
            self.state = 315
            self.match(GrammarParser.SEMICOLON)
            self.state = 316
            self.match(GrammarParser.SPACE)
            self.state = 317
            self.expression()
            self.state = 318
            self.match(GrammarParser.SPACE)
            self.state = 319
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 320
            self.match(GrammarParser.SPACE)
            self.state = 321
            self.statements()
            self.state = 322
            self.match(GrammarParser.SPACE)
            self.state = 323
            self.match(GrammarParser.BRACE_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GrammarParser.PRINT, 0)

        def PAR_LEFT(self):
            return self.getToken(GrammarParser.PAR_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def PAR_RIGHT(self):
            return self.getToken(GrammarParser.PAR_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)




    def print_statement(self):

        localctx = GrammarParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(GrammarParser.PRINT)
            self.state = 326
            self.match(GrammarParser.PAR_LEFT)
            self.state = 327
            self.expression()
            self.state = 328
            self.match(GrammarParser.PAR_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def logic_op(self):
            return self.getTypedRuleContext(GrammarParser.Logic_opContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = GrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.expression()
            self.state = 331
            self.match(GrammarParser.SPACE)
            self.state = 332
            self.logic_op()
            self.state = 333
            self.match(GrammarParser.SPACE)
            self.state = 334
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(GrammarParser.NOT_EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(GrammarParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(GrammarParser.GREATER_THAN, 0)

        def LESS_THAN_EQUALS(self):
            return self.getToken(GrammarParser.LESS_THAN_EQUALS, 0)

        def GREATER_THAN_EQUALS(self):
            return self.getToken(GrammarParser.GREATER_THAN_EQUALS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)




    def logic_op(self):

        localctx = GrammarParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





