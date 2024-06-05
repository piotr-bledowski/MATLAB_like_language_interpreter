from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from antlr4.tree.Tree import TerminalNodeImpl
import numpy as np

class VisitorImpl(GrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.output = ''

    def visitPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        return self.visitChildren(ctx)

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
                val = self.visitExpression(child)

        self.variables[var] = val
        #print(f'{var}: {val}')
        return self.visitChildren(ctx)

    def visitAddition(self, ctx:GrammarParser.AdditionContext):
        result = 0
        for child in ctx.children:
            #print(f'{child} ({type(child)})')
            if str(child).isnumeric():
                result += int(str(child))
            elif isinstance(child, GrammarParser.MultiplicationContext):
                result += self.visitMultiplication(child)
        return result

    def visitMultiplication(self, ctx:GrammarParser.MultiplicationContext):
        #print(self.visitChildren(ctx))
        result = 1
        for child in ctx.children:
            # print(f'{child} ({type(child)})')
            if str(child).isnumeric():
                result *= int(str(child))
            elif isinstance(child, GrammarParser.AdditionContext):
                result *= self.visitAddition(child)
        return result

    def visitPrint_statement(self, ctx: GrammarParser.Print_statementContext):
        for child in ctx.children:
            if isinstance(child, GrammarParser.ExpressionContext):
                if isinstance(child.getChild(0), TerminalNodeImpl):
                    self.output += f'{str(child.getChild(0))}\n'
                    print(str(child.getChild(0)))
                elif isinstance(child.getChild(0), GrammarParser.VariableContext):
                    self.output += f'{self.variables[str(child.getChild(0).getChild(0).getChild(0))]}\n'
                    print(self.variables[str(child.getChild(0).getChild(0).getChild(0))])
                # else:
                #     self.output += f'{self.variables[str(child.getChild(0).getChild(0).getChild(0))]}\n'
                #     print(self.variables[str(child.getChild(0).getChild(0).getChild(0))])

        return self.visitChildren(ctx)


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
