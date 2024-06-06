grammar Grammar;

program: statements+EOF;

addition: (NUMBER | variable_scalar | multiplication) SPACE* PLUS SPACE* (NUMBER | variable_scalar | multiplication);
subtraction: (NUMBER | variable_scalar | multiplication) SPACE* MINUS SPACE* (NUMBER | variable_scalar | multiplication);
multiplication: (NUMBER | variable_scalar) SPACE* MULTIPLICATION SPACE* (NUMBER | variable_scalar);
modulo_op: (NUMBER | variable) SPACE* MOD SPACE* (NUMBER | variable);
matmul: (matrix | variable_mat) SPACE* MULTIPLICATION SPACE* (matrix | variable_mat);
mat_add: (matrix | variable_mat) SPACE* PLUS SPACE* (matrix | variable_mat);
mat_scalar_mult: (matrix | variable_mat) SPACE* MULTIPLICATION SPACE* (NUMBER | variable_scalar)
    | (NUMBER | variable_scalar) SPACE* MULTIPLICATION SPACE* (matrix | variable_mat);
dot_product: (vector | variable_vec) SPACE* MULTIPLICATION SPACE* (vector | variable_vec);
vec_add: (vector | variable_vec) SPACE* PLUS SPACE* (vector | variable_vec);
vec_scalar_mult: (vector | variable_vec) SPACE* MULTIPLICATION SPACE* (NUMBER | variable_scalar)
    | (NUMBER | variable_scalar) SPACE* MULTIPLICATION SPACE* (vector | variable_vec);

sin: SIN PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
cos: COS PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
sqrt: SQRT PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
root: ROOT PAR_LEFT (NUMBER | variable_scalar) COMMA NUMBER PAR_RIGHT;
log: LOG PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;

vector: BRACKET_LEFT NUMBER (COMMA SPACE* NUMBER)* BRACKET_RIGHT;
matrix: BRACKET_LEFT vector (COMMA SPACE* vector)* BRACKET_RIGHT;

trig_func: sin | cos;

scalar_op: addition | subtraction | multiplication | modulo_op | sin | cos | sqrt | log | exp_func | abs_func | floor_func | ceil_func;

vector_op: dot_product | vec_add | vec_scalar_mult;

matrix_op: matmul | mat_add | mat_scalar_mult;

expression_scalar: scalar_op | variable_scalar | NUMBER;
expression_vec: vector_op | variable_vec | vector;
expression_mat: matrix_op | variable_mat | matrix;

built_in_func: trig_func | sqrt | log | exp_func | abs_func | ceil_func | floor_func;

expression: expression_scalar | expression_vec | expression_mat;

exp_func: EXP PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
abs_func: ABS PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
ceil_func: CEIL PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
floor_func: FLOOR PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;

arcsin_func: ARCSIN PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
arccos_func: ARCCOS PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
arctan_func: ARCTAN PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;

sinh_func: SINH PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;
cosh_func: COSH PAR_LEFT (NUMBER | variable_scalar) PAR_RIGHT;

factorial_func: (NUMBER | variable_scalar) FACTORIAL;

params: param SPACE* (COMMA SPACE* param)* | empty;
param: variable | variable ASSIGNMENT expression;
empty: ;
statements: statement | statement statements;
statement: SPACE* (assignment_statement | expression | if_statement | for_statement | print_statement | func_statement)? NEWLINE;

assignment_statement: variable_scalar SPACE* ASSIGNMENT SPACE* expression_scalar
    | variable_vec SPACE* ASSIGNMENT SPACE* expression_vec
    | variable_mat SPACE* ASSIGNMENT SPACE* expression_mat;
func_statement: FUNC SPACE* PAR_LEFT SPACE* params SPACE* PAR_RIGHT SPACE* BRACE_LEFT SPACE* statements SPACE* BRACE_RIGHT;
if_statement: IF SPACE* cond=condition ')' SPACE* BRACE_LEFT SPACE* NEWLINE* if_body=statements NEWLINE* BRACE_RIGHT | IF SPACE* cond=condition ')' SPACE* BRACE_LEFT SPACE* NEWLINE* if_body=statements SPACE* BRACE_RIGHT SPACE* NEWLINE* else_body=else_statement;
else_statement: ELSE SPACE* NEWLINE* body=statements NEWLINE* '}';
for_statement: FOR SPACE* init=assignment_statement SPACE* SEMICOLON SPACE* cond=condition SPACE* SEMICOLON SPACE* update=assignment_statement SPACE* ')' SPACE* BRACE_LEFT NEWLINE* SPACE* body=statements SPACE* NEWLINE* BRACE_RIGHT;
print_statement: PRINT SPACE* expression SPACE* ')';

condition: left=expression_scalar SPACE* op=logic_op SPACE* right=expression_scalar;

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

variable: variable_scalar | variable_vec | variable_mat;
variable_scalar: VEC_ID;
variable_vec: VEC_ID;
variable_mat: MAT_ID;

VEC_ID: [a-z_][a-zA-Z0-9_]*;
MAT_ID: [A-Z][a-zA-Z0-9_]*;

FUNC: 'func';
IF: 'if (';
ELSE: 'else {';
PRINT: 'print(';
FOR: 'for (';

NUMBER: [0-9][.]?[0-9]*;

SPACE: ' ';
NEWLINE: '\n';
