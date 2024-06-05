from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
from utils import InterpreterError, is_float
import numpy as np

class VisitorImpl(GrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.output = ''
        self.error_message = ''

    def visitChildren(self, node):
        try:
            return super().visitChildren(node)
        except InterpreterError as e:
            self.error_message = e.message
            return None

    def visitAssignment_statement(self, ctx:GrammarParser.Assignment_statementContext):
        var = None
        val = None

        for child in ctx.children:
            #print(f'{child} ({type(child)})')
            if isinstance(child, GrammarParser.VariableContext):
                #print(f'{child.getChild(0).getChild(0)} ({type(child.getChild(0).getChild(0))})')
                var = str(child.getChild(0).getChild(0))
            elif isinstance(child, GrammarParser.MatrixContext):
                pass
            elif isinstance(child, GrammarParser.ExpressionContext):
                if isinstance(child.getChild(0), TerminalNodeImpl):
                    if is_float(str(child.getChild(0))):
                        val = float(str(child.getChild(0)))
                    else:
                        raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')
                else:
                    val = self.visitExpression(child)

        self.variables[var] = val
        #print(f'{var}: {val}')
        return val

    def visitAddition(self, ctx:GrammarParser.AdditionContext):
        result = 0
        for child in ctx.children:
            #print(f'{child} ({type(child)})')
            if isinstance(child, TerminalNodeImpl):
                if is_float(str(child)):
                    result += float(str(child))
            elif isinstance(child, GrammarParser.VariableContext):
                var = self.variables[str(child.getChild(0).getChild(0))]
                result += var
            elif isinstance(child, GrammarParser.MultiplicationContext):
                result += self.visitMultiplication(child)
        return result

    def visitSubtraction(self, ctx:GrammarParser.SubtractionContext):
        l = None
        r = None
        for child in ctx.children:
            # print(f'{child} ({type(child)})')
            if isinstance(child, TerminalNodeImpl):
                if is_float(str(child)):
                    if l is None:
                        l = float(str(child))
                    elif r is None:
                        r = float(str(child))
            elif isinstance(child, GrammarParser.VariableContext):
                var = self.variables[str(child.getChild(0).getChild(0))]
                if l is None:
                    l = var
                elif r is None:
                    r = var
            elif isinstance(child, GrammarParser.MultiplicationContext):
                if l is None:
                    l = self.visitMultiplication(child)
                elif r is None:
                    r = self.visitMultiplication(child)

        return l - r



    def visitMultiplication(self, ctx:GrammarParser.MultiplicationContext):
        #print(self.visitChildren(ctx))
        result = 1.0
        for child in ctx.children:
            # print(f'{child} ({type(child)})')
            if isinstance(child, TerminalNodeImpl):
                if is_float(str(child)):
                    result *= float(str(child))
            elif isinstance(child, GrammarParser.VariableContext):
                var = self.variables[str(child.getChild(0).getChild(0))]
                result *= var
            elif isinstance(child, GrammarParser.MultiplicationContext):
                result *= self.visitMultiplication(child)
        return result

    def visitPrint_statement(self, ctx: GrammarParser.Print_statementContext):
        for child in ctx.children:
            if isinstance(child, GrammarParser.ExpressionContext):
                if isinstance(child.getChild(0), TerminalNodeImpl):
                    if child.getChild(0) is not None:
                        self.output += f'{str(child.getChild(0))}\n'
                        #print(str(child.getChild(0)))
                elif isinstance(child.getChild(0), GrammarParser.VariableContext):
                    if self.variables[str(child.getChild(0).getChild(0).getChild(0))] is not None:
                        self.output += f'{self.variables[str(child.getChild(0).getChild(0).getChild(0))]}\n'
                        #print(self.variables[str(child.getChild(0).getChild(0).getChild(0))])
                elif isinstance(child.getChild(0), GrammarParser.Built_in_funcContext):
                    self.output += f'{self.visitBuilt_in_func(child.getChild(0))}\n'
                    #print(str(self.visitBuilt_in_func(child.getChild(0))))

        return self.visitChildren(ctx)

    def visitSin(self, ctx:GrammarParser.SinContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.sin(float(self.variables[var]))
                    return np.sin(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.sin(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitCos(self, ctx:GrammarParser.CosContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.cos(float(self.variables[var]))
                    return np.cos(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.cos(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitSqrt(self, ctx:GrammarParser.CosContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.sqrt(float(self.variables[var]))
                    return np.sqrt(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.sqrt(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitLog(self, ctx:GrammarParser.CosContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.log(float(self.variables[var]))
                    return np.log(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.log(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitExp_func(self, ctx:GrammarParser.Exp_funcContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.exp(float(self.variables[var]))
                    return np.exp(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.exp(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitFloor_func(self, ctx:GrammarParser.Floor_funcContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.floor(float(self.variables[var]))
                    return np.floor(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.floor(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitCeil_func(self, ctx:GrammarParser.Floor_funcContext):
        for child in ctx.children:
            if not isinstance(child.getChild(0), TerminalNodeImpl):
                if isinstance(child.getChild(0), GrammarParser.VariableContext):
                    var = str(child.getChild(0).getChild(0).getChild(0))
                    #self.variables[var] = np.ceil(float(self.variables[var]))
                    return np.ceil(float(self.variables[var]))
            else:
                if is_float(str(child.getChild(0))):
                    return np.ceil(float(str(child.getChild(0))))
                else:
                    raise InterpreterError(f'{str(child.getChild(0))} is not a numeric value')

    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        cond_value = self.visitCondition(ctx.cond)
        if cond_value:
            self.visitStatements(ctx.if_body)
        else:
            self.visitStatements(ctx.else_body.body)

    def visitCondition(self, ctx:GrammarParser.ConditionContext):
        l = None
        r = None
        if isinstance(ctx.left.getChild(0), TerminalNodeImpl):
            if is_float(str(ctx.left.getChild(0))):
                l = float(str(ctx.left.getChild(0)))
            else:
                raise InterpreterError('Left operand is not a numeric expression')
        elif isinstance(ctx.left.getChild(0), GrammarParser.VariableContext):
            l = self.variables[str(ctx.left.getChild(0).getChild(0).getChild(0))]

        if isinstance(ctx.right.getChild(0), TerminalNodeImpl):
            if is_float(str(ctx.right.getChild(0))):
                r = float(str(ctx.right.getChild(0)))
            else:
                raise InterpreterError('Right operand is not a numeric expression')
        elif isinstance(ctx.right.getChild(0), GrammarParser.VariableContext):
            r = self.variables[str(ctx.right.getChild(0).getChild(0).getChild(0))]

        if str(ctx.op.getChild(0)) == '=':
            return l == r
        elif str(ctx.op.getChild(0)) == '<>':
            return l != r
        elif str(ctx.op.getChild(0)) == '>':
            return l > r
        elif str(ctx.op.getChild(0)) == '<':
            return l < r
        elif str(ctx.op.getChild(0)) == '>=':
            return l >= r
        elif str(ctx.op.getChild(0)) == '<=':
            return l <= r
        return None

    # def visitOperation(self, ctx:GrammarParser.OperationContext):
    #     if ctx.getChildCount() == 1:
        #     # Handle single elements (variable or number)
        #     if isinstance(ctx.getChild(0), GrammarParser.Variable_vecContext):
        #         # Access variable value from symbol table
        #         variable = ctx.getChild(0).getText()
        #         return self.variables.get(variable)
        #     else:
        #         # Return the number directly
        #         return float(ctx.getChild(0).getText())
        # else:
        #     # Handle binary operations
        #     left_value = self.visit(ctx.getChild(0))
        #     right_value = self.visit(ctx.getChild(2))
        #     operator = ctx.getChild(1).getText()
        #
        #     # Perform the operation based on the operator
        #     if operator == "+":
        #         return left_value + right_value
        #     elif operator == "-":
        #         return left_value - right_value
        #     elif operator == "*":
        #         return left_value * right_value
        #     elif operator == "/":
        #         # Handle division by zero
        #         if right_value == 0:
        #             raise ZeroDivisionError("Division by zero")
        #         return left_value / right_value
        #     elif operator == "^":
        #         return left_value ** right_value
        #     else:
        #         raise NotImplementedError("Unsupported operator: " + operator)
