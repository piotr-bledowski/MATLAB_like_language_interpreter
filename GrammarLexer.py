# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,34,177,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,
        1,25,1,26,1,26,5,26,140,8,26,10,26,12,26,143,9,26,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,3,31,166,8,31,1,31,5,31,169,8,31,10,31,
        12,31,172,9,31,1,32,1,32,1,33,1,33,0,0,34,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,
        57,29,59,30,61,31,63,32,65,33,67,34,1,0,3,3,0,65,90,95,95,97,122,
        4,0,48,57,65,90,95,95,97,122,1,0,48,57,179,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,
        0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,
        0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,
        0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,
        0,65,1,0,0,0,0,67,1,0,0,0,1,69,1,0,0,0,3,71,1,0,0,0,5,73,1,0,0,0,
        7,75,1,0,0,0,9,77,1,0,0,0,11,79,1,0,0,0,13,81,1,0,0,0,15,84,1,0,
        0,0,17,86,1,0,0,0,19,88,1,0,0,0,21,91,1,0,0,0,23,94,1,0,0,0,25,97,
        1,0,0,0,27,99,1,0,0,0,29,101,1,0,0,0,31,105,1,0,0,0,33,109,1,0,0,
        0,35,113,1,0,0,0,37,118,1,0,0,0,39,123,1,0,0,0,41,125,1,0,0,0,43,
        127,1,0,0,0,45,129,1,0,0,0,47,131,1,0,0,0,49,133,1,0,0,0,51,135,
        1,0,0,0,53,137,1,0,0,0,55,144,1,0,0,0,57,149,1,0,0,0,59,152,1,0,
        0,0,61,157,1,0,0,0,63,163,1,0,0,0,65,173,1,0,0,0,67,175,1,0,0,0,
        69,70,5,43,0,0,70,2,1,0,0,0,71,72,5,45,0,0,72,4,1,0,0,0,73,74,5,
        42,0,0,74,6,1,0,0,0,75,76,5,47,0,0,76,8,1,0,0,0,77,78,5,94,0,0,78,
        10,1,0,0,0,79,80,5,61,0,0,80,12,1,0,0,0,81,82,5,60,0,0,82,83,5,62,
        0,0,83,14,1,0,0,0,84,85,5,60,0,0,85,16,1,0,0,0,86,87,5,62,0,0,87,
        18,1,0,0,0,88,89,5,60,0,0,89,90,5,61,0,0,90,20,1,0,0,0,91,92,5,62,
        0,0,92,93,5,61,0,0,93,22,1,0,0,0,94,95,5,58,0,0,95,96,5,61,0,0,96,
        24,1,0,0,0,97,98,5,33,0,0,98,26,1,0,0,0,99,100,5,44,0,0,100,28,1,
        0,0,0,101,102,5,115,0,0,102,103,5,105,0,0,103,104,5,110,0,0,104,
        30,1,0,0,0,105,106,5,99,0,0,106,107,5,111,0,0,107,108,5,115,0,0,
        108,32,1,0,0,0,109,110,5,108,0,0,110,111,5,111,0,0,111,112,5,103,
        0,0,112,34,1,0,0,0,113,114,5,115,0,0,114,115,5,113,0,0,115,116,5,
        114,0,0,116,117,5,116,0,0,117,36,1,0,0,0,118,119,5,114,0,0,119,120,
        5,111,0,0,120,121,5,111,0,0,121,122,5,116,0,0,122,38,1,0,0,0,123,
        124,5,40,0,0,124,40,1,0,0,0,125,126,5,41,0,0,126,42,1,0,0,0,127,
        128,5,123,0,0,128,44,1,0,0,0,129,130,5,125,0,0,130,46,1,0,0,0,131,
        132,5,91,0,0,132,48,1,0,0,0,133,134,5,93,0,0,134,50,1,0,0,0,135,
        136,5,59,0,0,136,52,1,0,0,0,137,141,7,0,0,0,138,140,7,1,0,0,139,
        138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,
        54,1,0,0,0,143,141,1,0,0,0,144,145,5,102,0,0,145,146,5,117,0,0,146,
        147,5,110,0,0,147,148,5,99,0,0,148,56,1,0,0,0,149,150,5,105,0,0,
        150,151,5,102,0,0,151,58,1,0,0,0,152,153,5,101,0,0,153,154,5,108,
        0,0,154,155,5,115,0,0,155,156,5,101,0,0,156,60,1,0,0,0,157,158,5,
        112,0,0,158,159,5,114,0,0,159,160,5,105,0,0,160,161,5,110,0,0,161,
        162,5,116,0,0,162,62,1,0,0,0,163,165,7,2,0,0,164,166,9,0,0,0,165,
        164,1,0,0,0,165,166,1,0,0,0,166,170,1,0,0,0,167,169,7,2,0,0,168,
        167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,
        64,1,0,0,0,172,170,1,0,0,0,173,174,5,32,0,0,174,66,1,0,0,0,175,176,
        5,10,0,0,176,68,1,0,0,0,4,0,141,165,170,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MULTIPLICATION = 3
    DIVISION = 4
    POWER = 5
    EQUALS = 6
    NOT_EQUALS = 7
    LESS_THAN = 8
    GREATER_THAN = 9
    LESS_THAN_EQUALS = 10
    GREATER_THAN_EQUALS = 11
    ASSIGNMENT = 12
    FACTORIAL = 13
    COMMA = 14
    SIN = 15
    COS = 16
    LOG = 17
    SQRT = 18
    ROOT = 19
    PAR_LEFT = 20
    PAR_RIGHT = 21
    BRACE_LEFT = 22
    BRACE_RIGHT = 23
    BRACKET_LEFT = 24
    BRACKET_RIGHT = 25
    SEMICOLON = 26
    VARIABLE = 27
    FUNC = 28
    IF = 29
    ELSE = 30
    PRINT = 31
    NUMBER = 32
    SPACE = 33
    NEWLINE = 34

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'", "'='", "'<>'", "'<'", "'>'", 
            "'<='", "'>='", "':='", "'!'", "','", "'sin'", "'cos'", "'log'", 
            "'sqrt'", "'root'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "'func'", "'if'", "'else'", "'print'", "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "POWER", "EQUALS", 
            "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", 
            "GREATER_THAN_EQUALS", "ASSIGNMENT", "FACTORIAL", "COMMA", "SIN", 
            "COS", "LOG", "SQRT", "ROOT", "PAR_LEFT", "PAR_RIGHT", "BRACE_LEFT", 
            "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", "SEMICOLON", 
            "VARIABLE", "FUNC", "IF", "ELSE", "PRINT", "NUMBER", "SPACE", 
            "NEWLINE" ]

    ruleNames = [ "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "POWER", 
                  "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", 
                  "GREATER_THAN_EQUALS", "ASSIGNMENT", "FACTORIAL", "COMMA", 
                  "SIN", "COS", "LOG", "SQRT", "ROOT", "PAR_LEFT", "PAR_RIGHT", 
                  "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", 
                  "SEMICOLON", "VARIABLE", "FUNC", "IF", "ELSE", "PRINT", 
                  "NUMBER", "SPACE", "NEWLINE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


