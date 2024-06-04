grammar Grammar;

program: statements+EOF;

addition: (NUMBER | variable) SPACE* PLUS SPACE* (NUMBER | variable);
subtraction: (NUMBER | variable | addition) SPACE* MINUS SPACE* (NUMBER | variable | addition);
multiplication: (NUMBER | variable | addition | subtraction) SPACE* MULTIPLICATION SPACE* (NUMBER | variable | addition | subtraction);
matmul: (matrix | variable_mat) SPACE* MULTIPLICATION SPACE* (matrix | variable_mat);
dot_product: (vector | variable_vec) SPACE* MULTIPLICATION SPACE* (vector | variable_vec);

sin: SIN PAR_LEFT expression PAR_RIGHT;
cos: COS PAR_LEFT expression PAR_RIGHT;
sqrt: SQRT PAR_LEFT expression PAR_RIGHT;
root: ROOT PAR_LEFT expression COMMA NUMBER PAR_RIGHT;
log: LOG PAR_LEFT expression COMMA NUMBER PAR_RIGHT;

vector: BRACKET_LEFT NUMBER (COMMA SPACE* NUMBER)* BRACKET_RIGHT;
matrix: BRACKET_LEFT vector (COMMA SPACE* vector)* BRACKET_RIGHT;

trig_func: sin | cos;

scalar_op: addition | subtraction | multiplication;

operation: matmul | dot_product | scalar_op;

built_in_func: trig_func | sqrt | root | log | exp_func | abs_func | ceil_func | floor_func;

expression: built_in_func | operation | matrix | vector | variable | NUMBER;

exp_func: EXP PAR_LEFT expression PAR_RIGHT;
abs_func: ABS PAR_LEFT expression PAR_RIGHT;
ceil_func: CEIL PAR_LEFT expression PAR_RIGHT;
floor_func: FLOOR PAR_LEFT expression PAR_RIGHT;

arcsin_func: ARCSIN PAR_LEFT expression PAR_RIGHT;
arccos_func: ARCCOS PAR_LEFT expression PAR_RIGHT;
arctan_func: ARCTAN PAR_LEFT expression PAR_RIGHT;

sinh_func: SINH PAR_LEFT expression PAR_RIGHT;
cosh_func: COSH PAR_LEFT expression PAR_RIGHT;

factorial_func: expression FACTORIAL;
modulo_op: expression MOD expression;

params: param SPACE* (COMMA SPACE* param)* | empty;
param: variable | variable ASSIGNMENT expression;
empty: ;
statements: statement | statement statements;
statement: (assignment_statement | expression | if_statement | for_statement | print_statement | func_statement)? NEWLINE;

assignment_statement: variable SPACE* ASSIGNMENT SPACE* expression;
func_statement: FUNC SPACE* PAR_LEFT SPACE* params SPACE* PAR_RIGHT SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT;
if_statement: IF SPACE* condition SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT | IF SPACE* condition SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT SPACE* else_statement;
else_statement: ELSE SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT;
for_statement: FOR SPACE* variable_vec SPACE* ASSIGNMENT SPACE* expression SPACE* SEMICOLON SPACE* expression SPACE* SEMICOLON SPACE* expression SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT;
print_statement: PRINT SPACE* expression SPACE* ')';

condition: expression SPACE* logic_op SPACE* expression;

logic_op: EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_EQUALS | GREATER_THAN_EQUALS;

PLUS: '+';
MINUS: '-';
MULTIPLICATION: '*';
DIVISION: '/';
MOD: '%';
POWER: '^';
EQUALS: '=';
NOT_EQUALS: '<>';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_EQUALS: '<=';
GREATER_THAN_EQUALS: '>=';
ASSIGNMENT: ':=';
FACTORIAL: '!';
COMMA: ',';

EXP: 'exp';
ABS: 'abs';
CEIL: 'ceil';
FLOOR: 'floor';
SIN: 'sin';
COS: 'cos';
LOG: 'log';
SQRT: 'sqrt';
ROOT: 'root';
SINH: 'sinh';
COSH: 'cosh';
ARCSIN: 'arcsin';
ARCCOS: 'arccos';
ARCTAN: 'arctan';

PAR_LEFT: '(';
PAR_RIGHT: ')';
BRACE_LEFT: '{';
BRACE_RIGHT: '}';
BRACKET_LEFT: '[';
BRACKET_RIGHT: ']';
SEMICOLON: ';';

variable: variable_vec | variable_mat;
variable_vec: VEC_ID;
variable_mat: MAT_ID;

VEC_ID: [a-z_][a-zA-Z0-9_]*;
MAT_ID: [A-Z][a-zA-Z0-9_]*;

FUNC: 'func';
IF: 'if';
ELSE: 'else';
PRINT: 'print(';
FOR: 'for';

NUMBER: [0-9][.]?[0-9]*;

SPACE: ' ';
NEWLINE: '\n';
