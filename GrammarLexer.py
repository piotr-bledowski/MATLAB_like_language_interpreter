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
        4,0,46,265,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,
        7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,
        12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,
        29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,
        36,1,36,5,36,216,8,36,10,36,12,36,219,9,36,1,37,1,37,5,37,223,8,
        37,10,37,12,37,226,9,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,
        1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,43,1,43,3,43,254,8,43,1,43,5,43,257,8,43,10,43,
        12,43,260,9,43,1,44,1,44,1,45,1,45,0,0,46,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,
        57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,
        79,40,81,41,83,42,85,43,87,44,89,45,91,46,1,0,5,2,0,95,95,97,122,
        4,0,48,57,65,90,95,95,97,122,1,0,65,90,1,0,48,57,1,0,46,46,268,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,
        0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,
        0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,
        0,0,0,1,93,1,0,0,0,3,95,1,0,0,0,5,97,1,0,0,0,7,99,1,0,0,0,9,101,
        1,0,0,0,11,103,1,0,0,0,13,105,1,0,0,0,15,107,1,0,0,0,17,110,1,0,
        0,0,19,112,1,0,0,0,21,114,1,0,0,0,23,117,1,0,0,0,25,120,1,0,0,0,
        27,123,1,0,0,0,29,125,1,0,0,0,31,127,1,0,0,0,33,131,1,0,0,0,35,135,
        1,0,0,0,37,140,1,0,0,0,39,146,1,0,0,0,41,150,1,0,0,0,43,154,1,0,
        0,0,45,158,1,0,0,0,47,163,1,0,0,0,49,168,1,0,0,0,51,173,1,0,0,0,
        53,178,1,0,0,0,55,185,1,0,0,0,57,192,1,0,0,0,59,199,1,0,0,0,61,201,
        1,0,0,0,63,203,1,0,0,0,65,205,1,0,0,0,67,207,1,0,0,0,69,209,1,0,
        0,0,71,211,1,0,0,0,73,213,1,0,0,0,75,220,1,0,0,0,77,227,1,0,0,0,
        79,232,1,0,0,0,81,235,1,0,0,0,83,240,1,0,0,0,85,247,1,0,0,0,87,251,
        1,0,0,0,89,261,1,0,0,0,91,263,1,0,0,0,93,94,5,43,0,0,94,2,1,0,0,
        0,95,96,5,45,0,0,96,4,1,0,0,0,97,98,5,42,0,0,98,6,1,0,0,0,99,100,
        5,47,0,0,100,8,1,0,0,0,101,102,5,37,0,0,102,10,1,0,0,0,103,104,5,
        94,0,0,104,12,1,0,0,0,105,106,5,61,0,0,106,14,1,0,0,0,107,108,5,
        60,0,0,108,109,5,62,0,0,109,16,1,0,0,0,110,111,5,60,0,0,111,18,1,
        0,0,0,112,113,5,62,0,0,113,20,1,0,0,0,114,115,5,60,0,0,115,116,5,
        61,0,0,116,22,1,0,0,0,117,118,5,62,0,0,118,119,5,61,0,0,119,24,1,
        0,0,0,120,121,5,58,0,0,121,122,5,61,0,0,122,26,1,0,0,0,123,124,5,
        33,0,0,124,28,1,0,0,0,125,126,5,44,0,0,126,30,1,0,0,0,127,128,5,
        101,0,0,128,129,5,120,0,0,129,130,5,112,0,0,130,32,1,0,0,0,131,132,
        5,97,0,0,132,133,5,98,0,0,133,134,5,115,0,0,134,34,1,0,0,0,135,136,
        5,99,0,0,136,137,5,101,0,0,137,138,5,105,0,0,138,139,5,108,0,0,139,
        36,1,0,0,0,140,141,5,102,0,0,141,142,5,108,0,0,142,143,5,111,0,0,
        143,144,5,111,0,0,144,145,5,114,0,0,145,38,1,0,0,0,146,147,5,115,
        0,0,147,148,5,105,0,0,148,149,5,110,0,0,149,40,1,0,0,0,150,151,5,
        99,0,0,151,152,5,111,0,0,152,153,5,115,0,0,153,42,1,0,0,0,154,155,
        5,108,0,0,155,156,5,111,0,0,156,157,5,103,0,0,157,44,1,0,0,0,158,
        159,5,115,0,0,159,160,5,113,0,0,160,161,5,114,0,0,161,162,5,116,
        0,0,162,46,1,0,0,0,163,164,5,114,0,0,164,165,5,111,0,0,165,166,5,
        111,0,0,166,167,5,116,0,0,167,48,1,0,0,0,168,169,5,115,0,0,169,170,
        5,105,0,0,170,171,5,110,0,0,171,172,5,104,0,0,172,50,1,0,0,0,173,
        174,5,99,0,0,174,175,5,111,0,0,175,176,5,115,0,0,176,177,5,104,0,
        0,177,52,1,0,0,0,178,179,5,97,0,0,179,180,5,114,0,0,180,181,5,99,
        0,0,181,182,5,115,0,0,182,183,5,105,0,0,183,184,5,110,0,0,184,54,
        1,0,0,0,185,186,5,97,0,0,186,187,5,114,0,0,187,188,5,99,0,0,188,
        189,5,99,0,0,189,190,5,111,0,0,190,191,5,115,0,0,191,56,1,0,0,0,
        192,193,5,97,0,0,193,194,5,114,0,0,194,195,5,99,0,0,195,196,5,116,
        0,0,196,197,5,97,0,0,197,198,5,110,0,0,198,58,1,0,0,0,199,200,5,
        40,0,0,200,60,1,0,0,0,201,202,5,41,0,0,202,62,1,0,0,0,203,204,5,
        123,0,0,204,64,1,0,0,0,205,206,5,125,0,0,206,66,1,0,0,0,207,208,
        5,91,0,0,208,68,1,0,0,0,209,210,5,93,0,0,210,70,1,0,0,0,211,212,
        5,59,0,0,212,72,1,0,0,0,213,217,7,0,0,0,214,216,7,1,0,0,215,214,
        1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,74,1,
        0,0,0,219,217,1,0,0,0,220,224,7,2,0,0,221,223,7,1,0,0,222,221,1,
        0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,76,1,0,
        0,0,226,224,1,0,0,0,227,228,5,102,0,0,228,229,5,117,0,0,229,230,
        5,110,0,0,230,231,5,99,0,0,231,78,1,0,0,0,232,233,5,105,0,0,233,
        234,5,102,0,0,234,80,1,0,0,0,235,236,5,101,0,0,236,237,5,108,0,0,
        237,238,5,115,0,0,238,239,5,101,0,0,239,82,1,0,0,0,240,241,5,112,
        0,0,241,242,5,114,0,0,242,243,5,105,0,0,243,244,5,110,0,0,244,245,
        5,116,0,0,245,246,5,40,0,0,246,84,1,0,0,0,247,248,5,102,0,0,248,
        249,5,111,0,0,249,250,5,114,0,0,250,86,1,0,0,0,251,253,7,3,0,0,252,
        254,7,4,0,0,253,252,1,0,0,0,253,254,1,0,0,0,254,258,1,0,0,0,255,
        257,7,3,0,0,256,255,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,
        259,1,0,0,0,259,88,1,0,0,0,260,258,1,0,0,0,261,262,5,32,0,0,262,
        90,1,0,0,0,263,264,5,10,0,0,264,92,1,0,0,0,5,0,217,224,253,258,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MULTIPLICATION = 3
    DIVISION = 4
    MOD = 5
    POWER = 6
    EQUALS = 7
    NOT_EQUALS = 8
    LESS_THAN = 9
    GREATER_THAN = 10
    LESS_THAN_EQUALS = 11
    GREATER_THAN_EQUALS = 12
    ASSIGNMENT = 13
    FACTORIAL = 14
    COMMA = 15
    EXP = 16
    ABS = 17
    CEIL = 18
    FLOOR = 19
    SIN = 20
    COS = 21
    LOG = 22
    SQRT = 23
    ROOT = 24
    SINH = 25
    COSH = 26
    ARCSIN = 27
    ARCCOS = 28
    ARCTAN = 29
    PAR_LEFT = 30
    PAR_RIGHT = 31
    BRACE_LEFT = 32
    BRACE_RIGHT = 33
    BRACKET_LEFT = 34
    BRACKET_RIGHT = 35
    SEMICOLON = 36
    VEC_ID = 37
    MAT_ID = 38
    FUNC = 39
    IF = 40
    ELSE = 41
    PRINT = 42
    FOR = 43
    NUMBER = 44
    SPACE = 45
    NEWLINE = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'='", "'<>'", "'<'", 
            "'>'", "'<='", "'>='", "':='", "'!'", "','", "'exp'", "'abs'", 
            "'ceil'", "'floor'", "'sin'", "'cos'", "'log'", "'sqrt'", "'root'", 
            "'sinh'", "'cosh'", "'arcsin'", "'arccos'", "'arctan'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "';'", "'func'", "'if'", 
            "'else'", "'print('", "'for'", "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "MOD", "POWER", 
            "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", 
            "GREATER_THAN_EQUALS", "ASSIGNMENT", "FACTORIAL", "COMMA", "EXP", 
            "ABS", "CEIL", "FLOOR", "SIN", "COS", "LOG", "SQRT", "ROOT", 
            "SINH", "COSH", "ARCSIN", "ARCCOS", "ARCTAN", "PAR_LEFT", "PAR_RIGHT", 
            "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", 
            "SEMICOLON", "VEC_ID", "MAT_ID", "FUNC", "IF", "ELSE", "PRINT", 
            "FOR", "NUMBER", "SPACE", "NEWLINE" ]

    ruleNames = [ "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "MOD", 
                  "POWER", "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", 
                  "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", "ASSIGNMENT", 
                  "FACTORIAL", "COMMA", "EXP", "ABS", "CEIL", "FLOOR", "SIN", 
                  "COS", "LOG", "SQRT", "ROOT", "SINH", "COSH", "ARCSIN", 
                  "ARCCOS", "ARCTAN", "PAR_LEFT", "PAR_RIGHT", "BRACE_LEFT", 
                  "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", "SEMICOLON", 
                  "VEC_ID", "MAT_ID", "FUNC", "IF", "ELSE", "PRINT", "FOR", 
                  "NUMBER", "SPACE", "NEWLINE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


