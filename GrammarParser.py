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
        4,1,35,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,112,8,7,10,
        7,12,7,115,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,124,8,8,10,8,12,8,
        127,9,8,1,8,1,8,1,9,1,9,3,9,133,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        3,10,141,8,10,1,11,1,11,3,11,145,8,11,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
        20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,5,23,202,8,
        23,10,23,12,23,205,9,23,1,23,3,23,208,8,23,1,24,1,24,1,24,1,24,3,
        24,214,8,24,1,25,1,25,1,26,1,26,1,26,1,26,3,26,222,8,26,1,27,1,27,
        1,27,1,27,1,27,1,27,3,27,230,8,27,1,28,1,28,1,28,1,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,3,30,257,8,30,1,31,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,0,0,35,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,0,0,266,0,70,1,0,0,0,2,74,1,0,0,0,4,78,1,0,0,0,6,
        83,1,0,0,0,8,88,1,0,0,0,10,93,1,0,0,0,12,100,1,0,0,0,14,107,1,0,
        0,0,16,119,1,0,0,0,18,132,1,0,0,0,20,140,1,0,0,0,22,144,1,0,0,0,
        24,146,1,0,0,0,26,151,1,0,0,0,28,156,1,0,0,0,30,161,1,0,0,0,32,166,
        1,0,0,0,34,171,1,0,0,0,36,176,1,0,0,0,38,181,1,0,0,0,40,186,1,0,
        0,0,42,191,1,0,0,0,44,194,1,0,0,0,46,207,1,0,0,0,48,213,1,0,0,0,
        50,215,1,0,0,0,52,221,1,0,0,0,54,229,1,0,0,0,56,231,1,0,0,0,58,235,
        1,0,0,0,60,256,1,0,0,0,62,258,1,0,0,0,64,263,1,0,0,0,66,275,1,0,
        0,0,68,280,1,0,0,0,70,71,5,1,0,0,71,72,5,2,0,0,72,73,5,1,0,0,73,
        1,1,0,0,0,74,75,5,3,0,0,75,76,5,2,0,0,76,77,5,3,0,0,77,3,1,0,0,0,
        78,79,5,4,0,0,79,80,5,5,0,0,80,81,3,22,11,0,81,82,5,6,0,0,82,5,1,
        0,0,0,83,84,5,7,0,0,84,85,5,5,0,0,85,86,3,22,11,0,86,87,5,6,0,0,
        87,7,1,0,0,0,88,89,5,8,0,0,89,90,5,5,0,0,90,91,3,22,11,0,91,92,5,
        6,0,0,92,9,1,0,0,0,93,94,5,9,0,0,94,95,5,5,0,0,95,96,3,22,11,0,96,
        97,5,10,0,0,97,98,5,11,0,0,98,99,5,6,0,0,99,11,1,0,0,0,100,101,5,
        12,0,0,101,102,5,5,0,0,102,103,3,22,11,0,103,104,5,10,0,0,104,105,
        5,11,0,0,105,106,5,6,0,0,106,13,1,0,0,0,107,108,5,13,0,0,108,113,
        3,22,11,0,109,110,5,10,0,0,110,112,3,22,11,0,111,109,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,
        113,1,0,0,0,116,117,5,11,0,0,117,118,5,14,0,0,118,15,1,0,0,0,119,
        120,5,13,0,0,120,125,3,14,7,0,121,122,5,10,0,0,122,124,3,14,7,0,
        123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,
        126,128,1,0,0,0,127,125,1,0,0,0,128,129,5,14,0,0,129,17,1,0,0,0,
        130,133,3,4,2,0,131,133,3,6,3,0,132,130,1,0,0,0,132,131,1,0,0,0,
        133,19,1,0,0,0,134,141,3,18,9,0,135,141,3,4,2,0,136,141,3,6,3,0,
        137,141,3,8,4,0,138,141,3,10,5,0,139,141,3,12,6,0,140,134,1,0,0,
        0,140,135,1,0,0,0,140,136,1,0,0,0,140,137,1,0,0,0,140,138,1,0,0,
        0,140,139,1,0,0,0,141,21,1,0,0,0,142,145,3,20,10,0,143,145,5,11,
        0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,23,1,0,0,0,146,147,5,15,
        0,0,147,148,5,5,0,0,148,149,3,22,11,0,149,150,5,6,0,0,150,25,1,0,
        0,0,151,152,5,16,0,0,152,153,5,5,0,0,153,154,3,22,11,0,154,155,5,
        6,0,0,155,27,1,0,0,0,156,157,5,17,0,0,157,158,5,5,0,0,158,159,3,
        22,11,0,159,160,5,6,0,0,160,29,1,0,0,0,161,162,5,18,0,0,162,163,
        5,5,0,0,163,164,3,22,11,0,164,165,5,6,0,0,165,31,1,0,0,0,166,167,
        5,19,0,0,167,168,5,5,0,0,168,169,3,22,11,0,169,170,5,6,0,0,170,33,
        1,0,0,0,171,172,5,20,0,0,172,173,5,5,0,0,173,174,3,22,11,0,174,175,
        5,6,0,0,175,35,1,0,0,0,176,177,5,21,0,0,177,178,5,5,0,0,178,179,
        3,22,11,0,179,180,5,6,0,0,180,37,1,0,0,0,181,182,5,22,0,0,182,183,
        5,5,0,0,183,184,3,22,11,0,184,185,5,6,0,0,185,39,1,0,0,0,186,187,
        5,23,0,0,187,188,5,5,0,0,188,189,3,22,11,0,189,190,5,6,0,0,190,41,
        1,0,0,0,191,192,3,22,11,0,192,193,5,24,0,0,193,43,1,0,0,0,194,195,
        3,22,11,0,195,196,5,25,0,0,196,197,3,22,11,0,197,45,1,0,0,0,198,
        203,3,48,24,0,199,200,5,10,0,0,200,202,3,48,24,0,201,199,1,0,0,0,
        202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,208,1,0,0,0,
        205,203,1,0,0,0,206,208,3,50,25,0,207,198,1,0,0,0,207,206,1,0,0,
        0,208,47,1,0,0,0,209,214,5,26,0,0,210,211,5,26,0,0,211,212,5,27,
        0,0,212,214,3,22,11,0,213,209,1,0,0,0,213,210,1,0,0,0,214,49,1,0,
        0,0,215,216,1,0,0,0,216,51,1,0,0,0,217,222,3,54,27,0,218,219,3,54,
        27,0,219,220,3,52,26,0,220,222,1,0,0,0,221,217,1,0,0,0,221,218,1,
        0,0,0,222,53,1,0,0,0,223,230,3,56,28,0,224,230,3,22,11,0,225,230,
        3,60,30,0,226,230,3,64,32,0,227,230,3,66,33,0,228,230,3,58,29,0,
        229,223,1,0,0,0,229,224,1,0,0,0,229,225,1,0,0,0,229,226,1,0,0,0,
        229,227,1,0,0,0,229,228,1,0,0,0,230,55,1,0,0,0,231,232,5,26,0,0,
        232,233,5,27,0,0,233,234,3,22,11,0,234,57,1,0,0,0,235,236,5,28,0,
        0,236,237,5,5,0,0,237,238,3,46,23,0,238,239,5,6,0,0,239,240,5,29,
        0,0,240,241,3,52,26,0,241,242,5,30,0,0,242,59,1,0,0,0,243,244,5,
        31,0,0,244,245,3,68,34,0,245,246,5,29,0,0,246,247,3,52,26,0,247,
        248,5,30,0,0,248,257,1,0,0,0,249,250,5,31,0,0,250,251,3,68,34,0,
        251,252,5,29,0,0,252,253,3,52,26,0,253,254,5,30,0,0,254,255,3,62,
        31,0,255,257,1,0,0,0,256,243,1,0,0,0,256,249,1,0,0,0,257,61,1,0,
        0,0,258,259,5,32,0,0,259,260,5,29,0,0,260,261,3,52,26,0,261,262,
        5,30,0,0,262,63,1,0,0,0,263,264,5,33,0,0,264,265,5,26,0,0,265,266,
        5,27,0,0,266,267,3,22,11,0,267,268,5,34,0,0,268,269,3,22,11,0,269,
        270,5,34,0,0,270,271,3,22,11,0,271,272,5,29,0,0,272,273,3,52,26,
        0,273,274,5,30,0,0,274,65,1,0,0,0,275,276,5,35,0,0,276,277,5,5,0,
        0,277,278,3,22,11,0,278,279,5,6,0,0,279,67,1,0,0,0,280,281,3,50,
        25,0,281,69,1,0,0,0,11,113,125,132,140,144,203,207,213,221,229,256
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "MATRIX", "MULTIPLICATION", "VECTOR", 
                      "SIN", "PAR_LEFT", "PAR_RIGHT", "COS", "SQRT", "ROOT", 
                      "COMMA", "NUMBER", "LOG", "BRACKET_OPEN", "BRACKET_CLOSE", 
                      "EXP", "ABS", "CEIL", "FLOOR", "ARCSIN", "ARCCOS", 
                      "ARCTAN", "SINH", "COSH", "FACTORIAL", "MOD", "VARIABLE", 
                      "ASSIGNMENT", "FUNCTION", "BRACE_LEFT", "BRACE_RIGHT", 
                      "IF", "ELSE", "FOR", "SEMICOLON", "PRINT" ]

    RULE_matmul = 0
    RULE_dot_product = 1
    RULE_sin = 2
    RULE_cos = 3
    RULE_sqrt = 4
    RULE_root = 5
    RULE_log = 6
    RULE_vector = 7
    RULE_matrix = 8
    RULE_trig_func = 9
    RULE_built_in_func = 10
    RULE_expression = 11
    RULE_exp_func = 12
    RULE_abs_func = 13
    RULE_ceil_func = 14
    RULE_floor_func = 15
    RULE_arcsin_func = 16
    RULE_arccos_func = 17
    RULE_arctan_func = 18
    RULE_sinh_func = 19
    RULE_cosh_func = 20
    RULE_factorial_func = 21
    RULE_modulo_op = 22
    RULE_params = 23
    RULE_param = 24
    RULE_empty = 25
    RULE_statements = 26
    RULE_statement = 27
    RULE_assignment_statement = 28
    RULE_func_statement = 29
    RULE_if_statement = 30
    RULE_else_statement = 31
    RULE_for_statement = 32
    RULE_print_statement = 33
    RULE_condition = 34

    ruleNames =  [ "matmul", "dot_product", "sin", "cos", "sqrt", "root", 
                   "log", "vector", "matrix", "trig_func", "built_in_func", 
                   "expression", "exp_func", "abs_func", "ceil_func", "floor_func", 
                   "arcsin_func", "arccos_func", "arctan_func", "sinh_func", 
                   "cosh_func", "factorial_func", "modulo_op", "params", 
                   "param", "empty", "statements", "statement", "assignment_statement", 
                   "func_statement", "if_statement", "else_statement", "for_statement", 
                   "print_statement", "condition" ]

    EOF = Token.EOF
    MATRIX=1
    MULTIPLICATION=2
    VECTOR=3
    SIN=4
    PAR_LEFT=5
    PAR_RIGHT=6
    COS=7
    SQRT=8
    ROOT=9
    COMMA=10
    NUMBER=11
    LOG=12
    BRACKET_OPEN=13
    BRACKET_CLOSE=14
    EXP=15
    ABS=16
    CEIL=17
    FLOOR=18
    ARCSIN=19
    ARCCOS=20
    ARCTAN=21
    SINH=22
    COSH=23
    FACTORIAL=24
    MOD=25
    VARIABLE=26
    ASSIGNMENT=27
    FUNCTION=28
    BRACE_LEFT=29
    BRACE_RIGHT=30
    IF=31
    ELSE=32
    FOR=33
    SEMICOLON=34
    PRINT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MatmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATRIX(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MATRIX)
            else:
                return self.getToken(GrammarParser.MATRIX, i)

        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_matmul




    def matmul(self):

        localctx = GrammarParser.MatmulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_matmul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(GrammarParser.MATRIX)
            self.state = 71
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 72
            self.match(GrammarParser.MATRIX)
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

        def VECTOR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VECTOR)
            else:
                return self.getToken(GrammarParser.VECTOR, i)

        def MULTIPLICATION(self):
            return self.getToken(GrammarParser.MULTIPLICATION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_dot_product




    def dot_product(self):

        localctx = GrammarParser.Dot_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dot_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(GrammarParser.VECTOR)
            self.state = 75
            self.match(GrammarParser.MULTIPLICATION)
            self.state = 76
            self.match(GrammarParser.VECTOR)
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




    def sin(self):

        localctx = GrammarParser.SinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(GrammarParser.SIN)
            self.state = 79
            self.match(GrammarParser.PAR_LEFT)
            self.state = 80
            self.expression()
            self.state = 81
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




    def cos(self):

        localctx = GrammarParser.CosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(GrammarParser.COS)
            self.state = 84
            self.match(GrammarParser.PAR_LEFT)
            self.state = 85
            self.expression()
            self.state = 86
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




    def sqrt(self):

        localctx = GrammarParser.SqrtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sqrt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GrammarParser.SQRT)
            self.state = 89
            self.match(GrammarParser.PAR_LEFT)
            self.state = 90
            self.expression()
            self.state = 91
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




    def root(self):

        localctx = GrammarParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GrammarParser.ROOT)
            self.state = 94
            self.match(GrammarParser.PAR_LEFT)
            self.state = 95
            self.expression()
            self.state = 96
            self.match(GrammarParser.COMMA)
            self.state = 97
            self.match(GrammarParser.NUMBER)
            self.state = 98
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




    def log(self):

        localctx = GrammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GrammarParser.LOG)
            self.state = 101
            self.match(GrammarParser.PAR_LEFT)
            self.state = 102
            self.expression()
            self.state = 103
            self.match(GrammarParser.COMMA)
            self.state = 104
            self.match(GrammarParser.NUMBER)
            self.state = 105
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

        def BRACKET_OPEN(self):
            return self.getToken(GrammarParser.BRACKET_OPEN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(GrammarParser.BRACKET_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_vector




    def vector(self):

        localctx = GrammarParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GrammarParser.BRACKET_OPEN)
            self.state = 108
            self.expression()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 109
                self.match(GrammarParser.COMMA)
                self.state = 110
                self.expression()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(GrammarParser.NUMBER)
            self.state = 117
            self.match(GrammarParser.BRACKET_CLOSE)
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

        def BRACKET_OPEN(self):
            return self.getToken(GrammarParser.BRACKET_OPEN, 0)

        def vector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VectorContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VectorContext,i)


        def BRACKET_CLOSE(self):
            return self.getToken(GrammarParser.BRACKET_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_matrix




    def matrix(self):

        localctx = GrammarParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(GrammarParser.BRACKET_OPEN)
            self.state = 120
            self.vector()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 121
                self.match(GrammarParser.COMMA)
                self.state = 122
                self.vector()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(GrammarParser.BRACKET_CLOSE)
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




    def trig_func(self):

        localctx = GrammarParser.Trig_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_trig_func)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.sin()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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




    def built_in_func(self):

        localctx = GrammarParser.Built_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_built_in_func)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.trig_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.sin()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.cos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.sqrt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.root()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 139
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


        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_expression




    def expression(self):

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 7, 8, 9, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.built_in_func()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(GrammarParser.NUMBER)
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




    def exp_func(self):

        localctx = GrammarParser.Exp_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(GrammarParser.EXP)
            self.state = 147
            self.match(GrammarParser.PAR_LEFT)
            self.state = 148
            self.expression()
            self.state = 149
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




    def abs_func(self):

        localctx = GrammarParser.Abs_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_abs_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(GrammarParser.ABS)
            self.state = 152
            self.match(GrammarParser.PAR_LEFT)
            self.state = 153
            self.expression()
            self.state = 154
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




    def ceil_func(self):

        localctx = GrammarParser.Ceil_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ceil_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(GrammarParser.CEIL)
            self.state = 157
            self.match(GrammarParser.PAR_LEFT)
            self.state = 158
            self.expression()
            self.state = 159
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




    def floor_func(self):

        localctx = GrammarParser.Floor_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_floor_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(GrammarParser.FLOOR)
            self.state = 162
            self.match(GrammarParser.PAR_LEFT)
            self.state = 163
            self.expression()
            self.state = 164
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




    def arcsin_func(self):

        localctx = GrammarParser.Arcsin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arcsin_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(GrammarParser.ARCSIN)
            self.state = 167
            self.match(GrammarParser.PAR_LEFT)
            self.state = 168
            self.expression()
            self.state = 169
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




    def arccos_func(self):

        localctx = GrammarParser.Arccos_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arccos_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(GrammarParser.ARCCOS)
            self.state = 172
            self.match(GrammarParser.PAR_LEFT)
            self.state = 173
            self.expression()
            self.state = 174
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




    def arctan_func(self):

        localctx = GrammarParser.Arctan_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arctan_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(GrammarParser.ARCTAN)
            self.state = 177
            self.match(GrammarParser.PAR_LEFT)
            self.state = 178
            self.expression()
            self.state = 179
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




    def sinh_func(self):

        localctx = GrammarParser.Sinh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sinh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(GrammarParser.SINH)
            self.state = 182
            self.match(GrammarParser.PAR_LEFT)
            self.state = 183
            self.expression()
            self.state = 184
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




    def cosh_func(self):

        localctx = GrammarParser.Cosh_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cosh_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(GrammarParser.COSH)
            self.state = 187
            self.match(GrammarParser.PAR_LEFT)
            self.state = 188
            self.expression()
            self.state = 189
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




    def factorial_func(self):

        localctx = GrammarParser.Factorial_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factorial_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.expression()
            self.state = 192
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




    def modulo_op(self):

        localctx = GrammarParser.Modulo_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_modulo_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expression()
            self.state = 195
            self.match(GrammarParser.MOD)
            self.state = 196
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def empty(self):
            return self.getTypedRuleContext(GrammarParser.EmptyContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_params




    def params(self):

        localctx = GrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.param()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 199
                    self.match(GrammarParser.COMMA)
                    self.state = 200
                    self.param()
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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




    def param(self):

        localctx = GrammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(GrammarParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(GrammarParser.VARIABLE)
                self.state = 211
                self.match(GrammarParser.ASSIGNMENT)
                self.state = 212
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




    def empty(self):

        localctx = GrammarParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_empty)
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




    def statements(self):

        localctx = GrammarParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statements)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.statement()
                self.state = 219
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




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.assignment_statement()
                pass
            elif token in [4, 7, 8, 9, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.if_statement()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.for_statement()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.print_statement()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.func_statement()
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


    class Assignment_statementContext(ParserRuleContext):
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
            return GrammarParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = GrammarParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(GrammarParser.VARIABLE)
            self.state = 232
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 233
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

        def FUNCTION(self):
            return self.getToken(GrammarParser.FUNCTION, 0)

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




    def func_statement(self):

        localctx = GrammarParser.Func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(GrammarParser.FUNCTION)
            self.state = 236
            self.match(GrammarParser.PAR_LEFT)
            self.state = 237
            self.params()
            self.state = 238
            self.match(GrammarParser.PAR_RIGHT)
            self.state = 239
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 240
            self.statements()
            self.state = 241
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




    def if_statement(self):

        localctx = GrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_statement)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(GrammarParser.IF)
                self.state = 244
                self.condition()
                self.state = 245
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 246
                self.statements()
                self.state = 247
                self.match(GrammarParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(GrammarParser.IF)
                self.state = 250
                self.condition()
                self.state = 251
                self.match(GrammarParser.BRACE_LEFT)
                self.state = 252
                self.statements()
                self.state = 253
                self.match(GrammarParser.BRACE_RIGHT)
                self.state = 254
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

        def BRACE_LEFT(self):
            return self.getToken(GrammarParser.BRACE_LEFT, 0)

        def statements(self):
            return self.getTypedRuleContext(GrammarParser.StatementsContext,0)


        def BRACE_RIGHT(self):
            return self.getToken(GrammarParser.BRACE_RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_else_statement




    def else_statement(self):

        localctx = GrammarParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GrammarParser.ELSE)
            self.state = 259
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 260
            self.statements()
            self.state = 261
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




    def for_statement(self):

        localctx = GrammarParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(GrammarParser.FOR)
            self.state = 264
            self.match(GrammarParser.VARIABLE)
            self.state = 265
            self.match(GrammarParser.ASSIGNMENT)
            self.state = 266
            self.expression()
            self.state = 267
            self.match(GrammarParser.SEMICOLON)
            self.state = 268
            self.expression()
            self.state = 269
            self.match(GrammarParser.SEMICOLON)
            self.state = 270
            self.expression()
            self.state = 271
            self.match(GrammarParser.BRACE_LEFT)
            self.state = 272
            self.statements()
            self.state = 273
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




    def print_statement(self):

        localctx = GrammarParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(GrammarParser.PRINT)
            self.state = 276
            self.match(GrammarParser.PAR_LEFT)
            self.state = 277
            self.expression()
            self.state = 278
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

        def empty(self):
            return self.getTypedRuleContext(GrammarParser.EmptyContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_condition




    def condition(self):

        localctx = GrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.empty()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





