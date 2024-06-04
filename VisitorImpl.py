from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
import numpy as np

class VisitorImpl(GrammarVisitor):
    def __init__(self):
        self.variables = {}

    def visitAddition(self, ctx:GrammarParser.AdditionContext):
        print(self.visitChildren(ctx))
        return self.visitChildren(ctx)

    def visitOperation(self, ctx:GrammarParser.OperationContext):
        if ctx.getChildCount() == 1:
            # Handle single elements (variable or number)
            if isinstance(ctx.getChild(0), GrammarParser.IDContext):
                # Access variable value from symbol table
                variable = ctx.getChild(0).getText()
                return self.variables.get(variable)
            else:
                # Return the number directly
                return float(ctx.getChild(0).getText())
        else:
            # Handle binary operations
            left_value = self.visit(ctx.getChild(0))
            right_value = self.visit(ctx.getChild(2))
            operator = ctx.getChild(1).getText()

            # Perform the operation based on the operator
            if operator == "+":
                return left_value + right_value
            elif operator == "-":
                return left_value - right_value
            elif operator == "*":
                return left_value * right_value
            elif operator == "/":
                # Handle division by zero
                if right_value == 0:
                    raise ZeroDivisionError("Division by zero")
                return left_value / right_value
            elif operator == "^":
                return left_value ** right_value
            else:
                raise NotImplementedError("Unsupported operator: " + operator)
